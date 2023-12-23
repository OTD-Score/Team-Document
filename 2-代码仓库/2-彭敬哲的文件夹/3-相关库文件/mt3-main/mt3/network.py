# Copyright 2023 The MT3 Authors.
# 版权声明

# Licensed under the Apache License, Version 2.0 (the "License");
# 本代码基于Apache许可证2.0版本

# 你可能不会使用此文件，除非符合许可证的规定。
# 除非适用法律要求或书面同意，软件根据“原样”分发，不附带任何形式的担保或条件，无论是明示的还是暗示的。
# 请参阅许可证获取许可证的特定语言的副本详细信息和限制。
"""T5.1.1 Transformer model."""
# T5.1.1 Transformer模型

from typing import Any, Sequence

from flax import linen as nn
from flax import struct
import jax.numpy as jnp
from mt3 import layers

# 定义T5模型的全局超参数配置类
@struct.dataclass
class T5Config:
  """用于减少冗长的关键字参数的全局超参数配置"""
  # 词汇表大小
  vocab_size: int
  dtype: Any = jnp.float32
  emb_dim: int = 512
  num_heads: int = 8
  num_encoder_layers: int = 6
  num_decoder_layers: int = 6
  head_dim: int = 64
  mlp_dim: int = 2048
  mlp_activations: Sequence[str] = ('relu',)
  dropout_rate: float = 0.1
  logits_via_embedding: bool = False

# 定义Transformer编码器层
class EncoderLayer(nn.Module):
  """Transformer编码器层."""
  config: T5Config

  @nn.compact
  def __call__(self, inputs, encoder_mask=None, deterministic=False):
    cfg = self.config

    # 注意力块
    assert inputs.ndim == 3
    # 层归一化
    x = layers.LayerNorm(
        dtype=cfg.dtype, name='pre_attention_layer_norm')(
            inputs)
    # 多头自注意力机制
    x = layers.MultiHeadDotProductAttention(
        num_heads=cfg.num_heads,
        dtype=cfg.dtype,
        head_dim=cfg.head_dim,
        dropout_rate=cfg.dropout_rate,
        name='attention')(
            x, x, encoder_mask, deterministic=deterministic)
    # 丢弃
    x = nn.Dropout(
        rate=cfg.dropout_rate, broadcast_dims=(-2,))(
            x, deterministic=deterministic)
    # 残差连接
    x = x + inputs

    # MLP块
    y = layers.LayerNorm(dtype=cfg.dtype, name='pre_mlp_layer_norm')(x)
    # 多层感知机（MLP）块
    y = layers.MlpBlock(
        intermediate_dim=cfg.mlp_dim,
        activations=cfg.mlp_activations,
        intermediate_dropout_rate=cfg.dropout_rate,
        dtype=cfg.dtype,
        name='mlp',
    )(y, deterministic=deterministic)
    # 丢弃
    y = nn.Dropout(
        rate=cfg.dropout_rate, broadcast_dims=(-2,))(
            y, deterministic=deterministic)
    # 残差连接
    y = y + x

    return y

# 定义Transformer解码器层
class DecoderLayer(nn.Module):
  """Transformer解码器层，注意力机制与编码器交互."""
  config: T5Config

  @nn.compact
  def __call__(self,
               inputs,
               encoded,
               decoder_mask=None,
               encoder_decoder_mask=None,
               deterministic=False,
               decode=False,
               max_decode_length=None):
    cfg = self.config

    # 自注意力块
    x = layers.LayerNorm(
        dtype=cfg.dtype, name='pre_self_attention_layer_norm')(
            inputs)

    x = layers.MultiHeadDotProductAttention(
        num_heads=cfg.num_heads,
        dtype=cfg.dtype,
        head_dim=cfg.head_dim,
        dropout_rate=cfg.dropout_rate,
        name='self_attention')(
            x,
            x,
            decoder_mask,
            deterministic=deterministic,
            decode=decode)
    x = nn.Dropout(
        rate=cfg.dropout_rate, broadcast_dims=(-2,))(
            x, deterministic=deterministic)
    x = x + inputs

    # 编码器-解码器块
    y = layers.LayerNorm(
        dtype=cfg.dtype, name='pre_cross_attention_layer_norm')(
            x)
    y = layers.MultiHeadDotProductAttention(
        num_heads=cfg.num_heads,
        dtype=cfg.dtype,
        head_dim=cfg.head_dim,
        dropout_rate=cfg.dropout_rate,
        name='encoder_decoder_attention')(
            y, encoded, encoder_decoder_mask, deterministic=deterministic)
    y = nn.Dropout(
        rate=cfg.dropout_rate, broadcast_dims=(-2,))(
            y, deterministic=deterministic)
    y = y + x

    # MLP块
    z = layers.LayerNorm(dtype=cfg.dtype, name='pre_mlp_layer_norm')(y)
    z = layers.MlpBlock(
        intermediate_dim=cfg.mlp_dim,
        activations=cfg.mlp_activations,
        intermediate_dropout_rate=cfg.dropout_rate,
        dtype=cfg.dtype,
        name='mlp',
    )(z, deterministic=deterministic)
    z = nn.Dropout(
        rate=cfg.dropout_rate, broadcast_dims=(-2,))(
            z, deterministic=deterministic)
    z = z + y

    return z

# 定义Transformer编码器
class Encoder(nn.Module):
  """编码器层堆叠."""
  config: T5Config

  @nn.compact
  def __call__(self,
               encoder_input_tokens,
               encoder_mask=None,
               deterministic=False):
    cfg = self.config
    assert encoder_input_tokens.ndim == 3  # [batch, length, depth]

    seq_length = encoder_input_tokens.shape[-2]
    inputs_positions = jnp.arange(seq_length)[None, :]

    # [batch, length, depth] -> [batch, length, emb_dim]
    x = layers.DenseGeneral(  
        cfg.emb_dim,
        dtype=cfg.dtype,
        kernel_init=nn.linear.default_kernel_init,
        kernel_axes=('vocab', 'embed'),
        name='continuous_inputs_projection')(encoder_input_tokens)
    x = x + layers.FixedEmbed(features=cfg.emb_dim)(inputs_positions)
    x = nn.Dropout(
        rate=cfg.dropout_rate, broadcast_dims=(-2,))(
            x, deterministic=deterministic)
    x = x.astype(cfg.dtype)

    for lyr in range(cfg.num_encoder_layers):
      x = EncoderLayer(
          config=cfg,
          name=f'layers_{lyr}')(x, encoder_mask, deterministic)

    x = layers.LayerNorm(dtype=cfg.dtype, name='encoder_norm')(x)
    return nn.Dropout(rate=cfg.dropout_rate)(x, deterministic=deterministic)

# 定义Transformer解码器
class Decoder(nn.Module):
  """解码器层堆叠，作为编码器-解码器架构的一部分."""
  config: T5Config

  @nn.compact
  def __call__(self,
               encoded,
               decoder_input_tokens,
               decoder_positions=None,
               decoder_mask=None,
               encoder_decoder_mask=None,
               deterministic=False,
               decode=False,
               max_decode_length=None):
    cfg = self.config
    assert decoder_input_tokens.ndim == 2  # [batch, len]

    seq_length = decoder_input_tokens.shape[-1]
    decoder_positions = jnp.arange(seq_length)[None, :]

    # [batch, length] -> [batch, length, emb_dim]
    y = layers.Embed(  
        num_embeddings=cfg.vocab_size,
        features=cfg.emb_dim,
        dtype=cfg.dtype,
        attend_dtype=jnp.float32,  
        embedding_init=nn.initializers.normal(stddev=1.0),
        one_hot=True,
        name='token_embedder')(decoder_input_tokens.astype('int32'))
    y = y + layers.FixedEmbed(features=cfg.emb_dim)(
        decoder_positions, decode=decode)
    y = nn.Dropout(
        rate=cfg.dropout_rate, broadcast_dims=(-2,))(
            y, deterministic=deterministic)
    y = y.astype(cfg.dtype)

    for lyr in range(cfg.num_decoder_layers):
      y = DecoderLayer(
          config=cfg, name=f'layers_{lyr}')(
              y,
              encoded,
              decoder_mask=decoder_mask,
              encoder_decoder_mask=encoder_decoder_mask,
              deterministic=deterministic,
              decode=decode,
              max_decode_length=max_decode_length)

    y = layers.LayerNorm(dtype=cfg.dtype, name='decoder_norm')(y)
    y = nn.Dropout(
        rate=cfg.dropout_rate, broadcast_dims=(-2,))(
            y, deterministic=deterministic)

    # [batch, length, emb_dim] -> [batch, length, vocab_size]
    if cfg.logits_via_embedding:
      logits = self.shared_embedding.attend(y)
      logits = logits / jnp.sqrt(y.shape[-1])
    else:
      logits = layers.DenseGeneral(
          cfg.vocab_size,
          dtype=jnp.float32,  
          kernel_axes=('embed', 'vocab'),
          name='logits_dense')(
              y)
    return logits

# 定义Transformer模型
class Transformer(nn.Module):
  """编码器-解码器 Transformer 模型."""
  config: T5Config

  def setup(self):
    cfg = self.config

    self.encoder = Encoder(config=cfg)
    self.decoder = Decoder(config=cfg)

  def encode(self,
             encoder_input_tokens,
             encoder_segment_ids=None,
             enable_dropout=True):
    """对输入应用Transformer编码器分支."""
    cfg = self.config
    assert encoder_input_tokens.ndim == 3  

    encoder_mask = layers.make_attention_mask(
        jnp.ones(encoder_input_tokens.shape[:-1]),
        jnp.ones(encoder_input_tokens.shape[:-1]),
        dtype=cfg.dtype)
    if encoder_segment_ids is not None:
      encoder_mask = layers.combine_masks(
          encoder_mask,
          layers.make_attention_mask(
              encoder_segment_ids,
              encoder_segment_ids,
              jnp.equal,
              dtype=cfg.dtype))

    return self.encoder(
        encoder_input_tokens, encoder_mask, deterministic=not enable_dropout)

  def decode(
      self,
      encoded,
      encoder_input_tokens,  
      decoder_input_tokens,
      decoder_target_tokens,
      encoder_segment_ids=None,
      decoder_segment_ids=None,
      decoder_positions=None,
      enable_dropout=True,
      decode=False,
      max_decode_length=None):
    """对编码输入和目标应用Transformer解码器分支."""
    cfg = self.config

    if decode:
      decoder_mask = None
      encoder_decoder_mask = layers.make_attention_mask(
          jnp.ones_like(decoder_target_tokens),
          jnp.ones(encoder_input_tokens.shape[:-1]),
          dtype=cfg.dtype)
    else:
      decoder_mask = layers.make_decoder_mask(
          decoder_target_tokens=decoder_target_tokens,
          dtype=cfg.dtype,
          decoder_segment_ids=decoder_segment_ids)
      encoder_decoder_mask = layers.make_attention_mask(
          decoder_target_tokens > 0,
          jnp.ones(encoder_input_tokens.shape[:-1]),
          dtype=cfg.dtype)

    if encoder_segment_ids is not None:
      if decode:
        raise ValueError(
            '在解码期间，不应使用分段，但`encoder_segment_ids`被传递到`Transformer.decode`。')

      encoder_decoder_mask = layers.combine_masks(
          encoder_decoder_mask,
          layers.make_attention_mask(
              decoder_segment_ids,
              encoder_segment_ids,
              jnp.equal,
              dtype=cfg.dtype))

    logits = self.decoder(
        encoded,
        decoder_input_tokens=decoder_input_tokens,
        decoder_positions=decoder_positions,
        decoder_mask=decoder_mask,
        encoder_decoder_mask=encoder_decoder_mask,
        deterministic=not enable_dropout,
        decode=decode,
        max_decode_length=max_decode_length)
    return logits.astype(self.config.dtype)

  def __call__(self,
               encoder_input_tokens,
               decoder_input_tokens,
               decoder_target_tokens,
               encoder_segment_ids=None,
               decoder_segment_ids=None,
               encoder_positions=None,
               decoder_positions=None,
               *,
               enable_dropout: bool = True,
               decode: bool = False):
    """对输入应用Transformer模型.

    该方法需要decoder_target_tokens和decoder_input_tokens，decoder_input_tokens是前者的位移版本。
    对于打包的数据集，通常应用了额外的处理。例如，每个序列的第一个元素的ID是0，而不是上一个序列的位移EOS ID。

    参数:
      encoder_input_tokens: 输入数据到编码器.
      decoder_input_tokens: 输入到解码器的标记.
      decoder_target_tokens: 解码器的目标标记.
      encoder_segment_ids: 用于打包示例的编码器分段信息.
      decoder_segment_ids: 用于打包示例的解码器分段信息.
      encoder_positions: 打包示例的编码器子序列位置.
      decoder_positions: 打包示例的解码器子序列位置.
      enable_dropout: 如果设置为True，则启用丢弃.
      decode: 是否准备和使用自回归缓存.

    返回:
      完整Transformer模型的logits数组.
    """
    encoded = self.encode(
        encoder_input_tokens,
        encoder_segment_ids=encoder_segment_ids,
        enable_dropout=enable_dropout)

    return self.decode(
        encoded,
        encoder_input_tokens,  
        decoder_input_tokens,
        decoder_target_tokens,
        encoder_segment_ids=encoder_segment_ids,
        decoder_segment_ids=decoder_segment_ids,
        decoder_positions=decoder_positions,
        enable_dropout=enable_dropout,
        decode=decode)

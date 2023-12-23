# 版权声明
# 2023 年 MT3 作者
#
# 根据 Apache 许可证 2.0 版（"许可证"）获得许可;
# 除非符合许可证的规定，否则您不能使用此文件。
# 您可以在以下网址获取许可证的副本：
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# 除非适用法律要求或书面同意，本软件是基于"按原样"的基础分发的，
# 没有任何明示或暗示的担保或条件。
# 有关特定语言的权限和限制，请参阅许可证。

"""连续输入的特征转换器和模型。"""

from typing import Mapping
import seqio
from t5x import decoding
from t5x import models
import tensorflow as tf

# 连续输入的特征转换器类
class ContinuousInputsEncDecFeatureConverter(seqio.FeatureConverter):
  """具有连续输入的编码器-解码器的特征转换器。"""

  TASK_FEATURES = {
      "inputs": seqio.FeatureConverter.FeatureSpec(dtype=tf.float32, rank=2),
      "targets": seqio.FeatureConverter.FeatureSpec(dtype=tf.int32),
  }
  MODEL_FEATURES = {
      "encoder_input_tokens":
          seqio.FeatureConverter.FeatureSpec(dtype=tf.float32, rank=2),
      "decoder_target_tokens":
          seqio.FeatureConverter.FeatureSpec(dtype=tf.int32),
      "decoder_input_tokens":
          seqio.FeatureConverter.FeatureSpec(dtype=tf.int32),
      "decoder_loss_weights":
          seqio.FeatureConverter.FeatureSpec(dtype=tf.int32),
  }
  PACKING_FEATURE_DTYPES = {
      "encoder_segment_ids": tf.int32,
      "decoder_segment_ids": tf.int32,
      "encoder_positions": tf.int32,
      "decoder_positions": tf.int32
  }

  def _convert_features(
      self, ds: tf.data.Dataset,
      task_feature_lengths: Mapping[str, int]) -> tf.data.Dataset:
    """将数据集转换为用于编码器-解码器模型的格式。

    转换过程包括三个步骤：

    1. 对 `task_feature_lengths` 中的每个特征进行修剪/填充，
       根据 self.pack 的值进行可选的打包。
    2. 将 "inputs" 字段映射到编码器输入，将 "targets" 映射到解码器输入（经过移位）和目标。
    3. 通过检查 self.pack 的值，决定是否对数据集进行打包。

    `task_feature_lengths` 中的所有键都应该存在于输入数据集中，
    输入数据集可能包含一些不在 `task_feature_lengths` 中的额外特征。
    这些特征将不包含在输出数据集中。常见的情况是 "inputs_pretokenized"
    和 "targets_pretokenized" 字段。

    Args:
      ds: 要转换的输入 tf.data.Dataset。
      task_feature_lengths: 特征和其长度的映射。

    Returns:
      ds: 转换后的数据集。
    """

    def convert_example(
        features: Mapping[str, tf.Tensor]) -> Mapping[str, tf.Tensor]:
      # 对于打包的数据集，targets_segment_id 仅在其中。
      decoder_input_tokens = seqio.autoregressive_inputs(
          features["targets"],
          sequence_id=features.get("targets_segment_ids", None))

      d = {"encoder_input_tokens": features["inputs"],
           "decoder_target_tokens": features["targets"],
           "decoder_input_tokens": decoder_input_tokens,
           # 计算除填充位置之外的所有位置的损失。
           "decoder_loss_weights":
               seqio.non_padding_position(features["targets"])}

      if self.pack:
        d["encoder_segment_ids"] = features["inputs_segment_ids"]
        d["decoder_segment_ids"] = features["targets_segment_ids"]
        d["encoder_positions"] = features["inputs_positions"]
        d["decoder_positions"] = features["targets_positions"]

      return d

    ds = self._pack_or_pad(ds, task_feature_lengths)
    return ds.map(
        convert_example, num_parallel_calls=tf.data.experimental.AUTOTUNE)

  def get_model_feature_lengths(
      self, task_feature_lengths: Mapping[str, int]) -> Mapping[str, int]:
    """定义输入和输出特征之间的长度关系。"""
    encoder_length = task_feature_lengths["inputs"]
    decoder_length = task_feature_lengths["targets"]

    model_feature_lengths = {
        "encoder_input_tokens": encoder_length,
        "decoder_target_tokens": decoder_length,
        "decoder_input_tokens": decoder_length,
        "decoder_loss_weights": decoder_length
    }
    if self.pack:
      model_feature_lengths["encoder_segment_ids"] = encoder_length
      model_feature_lengths["decoder_segment_ids"] = decoder_length
      model_feature_lengths["encoder_positions"] = encoder_length
      model_feature_lengths["decoder_positions"] = decoder_length

    return model_feature_lengths


# 具有连续输入的编码器-解码器模型类
class ContinuousInputsEncoderDecoderModel(models.EncoderDecoderModel):
  """具有连续输入的编码器-解码器模型。"""

  FEATURE_CONVERTER_CLS = ContinuousInputsEncDecFeatureConverter

  def __init__(self, module, input_vocabulary, output_vocabulary, optimizer_def,
               input_depth, decode_fn=decoding.beam_search, label_smoothing=0.0,
               z_loss=0.0, loss_normalizing_factor=None):
    super().__init__(
        module=module,
        input_vocabulary=input_vocabulary,
        output_vocabulary=output_vocabulary,
        optimizer_def=optimizer_def,
        decode_fn=decode_fn,
        label_smoothing=label_smoothing,
        z_loss=z_loss,
        loss_normalizing_factor=loss_normalizing_factor)
    self._input_depth = input_depth

  def get_initial_variables(self, rng, input_shapes, input_types=None):
    """为了绕过评估/推断不能处理秩为 3 的输入的问题，使用 hacky 覆盖。"""
    encoder_shape = input_shapes["encoder_input_tokens"]
    if len(encoder_shape) == 2:
      input_shapes = {
          "encoder_input_tokens": (*encoder_shape, self._input_depth),
          **{k: v for k, v in input_shapes.items()
             if k != "encoder_input_tokens"}
      }
    else:
      assert encoder_shape[-1] == self._input_depth
    return super().get_initial_variables(
        rng=rng, input_shapes=input_shapes, input_types=input_types)

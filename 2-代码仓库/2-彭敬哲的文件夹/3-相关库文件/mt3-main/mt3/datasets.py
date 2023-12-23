# 版权声明
# 使用 Apache License, Version 2.0 授权许可
# 许可详情可在 http://www.apache.org/licenses/LICENSE-2.0 获取

# 导入必要的库和模块
import dataclasses  # 用于创建不可变对象的装饰器
from typing import Mapping, Sequence, Union  # 用于类型提示

from mt3 import note_sequences  # 导入自定义的模块
import tensorflow as tf  # 导入 TensorFlow 库


# 定义一个用于推断和评估的数据集拆分配置类
@dataclasses.dataclass
class InferEvalSplit:
  # 数据集拆分在字典中的键名
  name: str
  # 任务名称后缀（每个评估拆分是一个单独的任务）
  suffix: str
  # 是否包含在所有评估任务的混合中
  include_in_mixture: bool = True
  

# 定义一个用于音乐转录数据集的配置类
@dataclasses.dataclass
class DatasetConfig:
  """音乐转录数据集的配置类."""
  # 数据集名称
  name: str
  # 拆分名称到路径的映射
  paths: Mapping[str, str]
  # 特征名称到特征的映射
  features: Mapping[str, Union[tf.io.FixedLenFeature,
                               tf.io.FixedLenSequenceFeature]]
  # 训练拆分名称
  train_split: str
  # 训练评估拆分名称
  train_eval_split: str
  # 推断评估拆分规格的列表
  infer_eval_splits: Sequence[InferEvalSplit]
  # 用于指标的轨迹规格的列表
  track_specs: Sequence[note_sequences.TrackSpec] = dataclasses.field(
      default_factory=list)


# MAESTROV1_CONFIG 是一个音乐转录数据集的配置示例
MAESTROV1_CONFIG = DatasetConfig(
    name='maestrov1',
    paths={
        'train':
            'gs://magentadata/datasets/maestro/v1.0.0/maestro-v1.0.0_ns_wav_train.tfrecord-?????-of-00010',
        'train_subset':
            'gs://magentadata/datasets/maestro/v1.0.0/maestro-v1.0.0_ns_wav_train.tfrecord-00002-of-00010',
        'validation':
            'gs://magentadata/datasets/maestro/v1.0.0/maestro-v1.0.0_ns_wav_validation.tfrecord-?????-of-00010',
        'validation_subset':
            'gs://magentadata/datasets/maestro/v1.0.0/maestro-v1.0.0_ns_wav_validation.tfrecord-0000[06]-of-00010',
        'test':
            'gs://magentadata/datasets/maestro/v1.0.0/maestro-v1.0.0_ns_wav_test.tfrecord-?????-of-00010'
    },
    features={
        'audio': tf.io.FixedLenFeature([], dtype=tf.string),
        'sequence': tf.io.FixedLenFeature([], dtype=tf.string),
        'id': tf.io.FixedLenFeature([], dtype=tf.string)
    },
    train_split='train',
    train_eval_split='validation_subset',
    infer_eval_splits=[
        InferEvalSplit(name='train', suffix='eval_train_full',
                       include_in_mixture=False),
        InferEvalSplit(name='train_subset', suffix='eval_train'),
        InferEvalSplit(name='validation', suffix='validation_full',
                       include_in_mixture=False),
        InferEvalSplit(name='validation_subset', suffix='validation'),
        InferEvalSplit(name='test', suffix='test', include_in_mixture=False)
    ])


# MAESTROV3_CONFIG 是一个音乐转录数据集的配置示例
MAESTROV3_CONFIG = DatasetConfig(
    name='maestrov3',
    paths={
        'train':
            'gs://magentadata/datasets/maestro/v3.0.0/maestro-v3.0.0_ns_wav_train.tfrecord-?????-of-00025',
        'train_subset':
            'gs://magentadata/datasets/maestro/v3.0.0/maestro-v3.0.0_ns_wav_train.tfrecord-00004-of-00025',
        'validation':
            'gs://magentadata/datasets/maestro/v3.0.0/maestro-v3.0.0_ns_wav_validation.tfrecord-?????-of-00025',
        'validation_subset':
            'gs://magentadata/datasets/maestro/v3.0.0/maestro-v3.0.0_ns_wav_validation.tfrecord-0002?-of-00025',
        'test':
            'gs://magentadata/datasets/maestro/v3.0.0/maestro-v3.0.0_ns_wav_test.tfrecord-?????-of-00025'
    },
    features={
        'audio': tf.io.FixedLenFeature([], dtype=tf.string),  # 音频特征
        'sequence': tf.io.FixedLenFeature([], dtype=tf.string),  # 序列特征
        'id': tf.io.FixedLenFeature([], dtype=tf.string)  # ID特征
    },
    train_split='train',  # 训练数据集拆分
    train_eval_split='validation_subset',  # 训练评估拆分
    infer_eval_splits=[
        InferEvalSplit(name='train', suffix='eval_train_full',
                       include_in_mixture=False),  # 推断评估拆分规格
        InferEvalSplit(name='train_subset', suffix='eval_train'),  # 推断评估拆分规格
        InferEvalSplit(name='validation', suffix='validation_full',
                       include_in_mixture=False),  # 推断评估拆分规格
        InferEvalSplit(name='validation_subset', suffix='validation'),  # 推断评估拆分规格
        InferEvalSplit(name='test', suffix='test', include_in_mixture=False)  # 推断评估拆分规格
    ])


# GUITARSET_CONFIG 是一个吉他数据集的配置示例
GUITARSET_CONFIG = DatasetConfig(
    name='guitarset',
    paths={
        'train':
            'gs://mt3/data/datasets/guitarset/train.tfrecord-?????-of-00019',
        'validation':
            'gs://mt3/data/datasets/guitarset/validation.tfrecord-?????-of-00006',
    },
    features={
        'sequence': tf.io.FixedLenFeature([], dtype=tf.string),  # 序列特征
        'audio': tf.io.FixedLenFeature([], dtype=tf.string),  # 音频特征
        'velocity_range': tf.io.FixedLenFeature([], dtype=tf.string),  # 速度范围特征
        'id': tf.io.FixedLenFeature([], dtype=tf.string),  # ID特征
    },
    train_split='train',  # 训练数据集拆分
    train_eval_split='validation',  # 训练评估拆分
    infer_eval_splits=[
        InferEvalSplit(name='train', suffix='eval_train'),  # 推断评估拆分规格
        InferEvalSplit(name='validation', suffix='validation')  # 推断评估拆分规格
    ])


# URMP_CONFIG 是一个URMP数据集的配置示例
URMP_CONFIG = DatasetConfig(
    name='urmp',
    paths={
        'train': 'gs://mt3/data/datasets/urmp/train.tfrecord',  # 训练数据集路径
        'validation': 'gs://mt3/data/datasets/urmp/validation.tfrecord',  # 验证数据集路径
    },
    features={
        'id': tf.io.FixedLenFeature([], dtype=tf.string),  # ID特征
        'tracks': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.int64, allow_missing=True),  # 轨道序列特征
        'inst_names': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.string, allow_missing=True),  # 乐器名称序列特征
        'audio': tf.io.FixedLenFeature([], dtype=tf.string),  # 音频特征
        'sequence': tf.io.FixedLenFeature([], dtype=tf.string),  # 序列特征
        'instrument_sequences': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.string, allow_missing=True),  # 乐器序列特征
    },
    train_split='train',  # 训练数据集拆分
    train_eval_split='validation',  # 训练评估拆分
    infer_eval_splits=[
        InferEvalSplit(name='train', suffix='eval_train'),  # 推断评估拆分规格
        InferEvalSplit(name='validation', suffix='validation')  # 推断评估拆分规格
    ])


# MUSICNET_CONFIG 是一个MusicNet数据集的配置示例
MUSICNET_CONFIG = DatasetConfig(
    name='musicnet',
    paths={
        'train':
            'gs://mt3/data/datasets/musicnet/musicnet-train.tfrecord-?????-of-00036',
        'validation':
            'gs://mt3/data/datasets/musicnet/musicnet-validation.tfrecord-?????-of-00005',
        'test':
            'gs://mt3/data/datasets/musicnet/musicnet-test.tfrecord-?????-of-00003'
    },
    features={
        'id': tf.io.FixedLenFeature([], dtype=tf.string),  # ID特征
        'sample_rate': tf.io.FixedLenFeature([], dtype=tf.float32),  # 采样率特征
        'audio': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.float32, allow_missing=True),  # 音频序列特征
        'sequence': tf.io.FixedLenFeature([], dtype=tf.string)  # 序列特征
    },
    train_split='train',  # 训练数据集拆分
    train_eval_split='validation',  # 训练评估拆分
    infer_eval_splits=[
        InferEvalSplit(name='train', suffix='eval_train'),  # 推断评估拆分规格
        InferEvalSplit(name='validation', suffix='validation'),  # 推断评估拆分规格
        InferEvalSplit(name='test', suffix='test', include_in_mixture=False)  # 推断评估拆分规格
    ])


# MUSICNET_EM_CONFIG 是一个MusicNet EM数据集的配置示例
MUSICNET_EM_CONFIG = DatasetConfig(
    name='musicnet_em',
    paths={
        'train':
            'gs://mt3/data/datasets/musicnet_em/train.tfrecord-?????-of-00103',
        'validation':
            'gs://mt3/data/datasets/musicnet_em/validation.tfrecord-?????-of-00005',
        'test':
            'gs://mt3/data/datasets/musicnet_em/test.tfrecord-?????-of-00006'
    },
    features={
        'id': tf.io.FixedLenFeature([], dtype=tf.string),  # ID特征
        'sample_rate': tf.io.FixedLenFeature([], dtype=tf.float32),  # 采样率特征
        'audio': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.float32, allow_missing=True),  # 音频序列特征
        'sequence': tf.io.FixedLenFeature([], dtype=tf.string)  # 序列特征
    },
    train_split='train',  # 训练数据集拆分
    train_eval_split='validation',  # 训练评估拆分
    infer_eval_splits=[
        InferEvalSplit(name='train', suffix='eval_train'),  # 推断评估拆分规格
        InferEvalSplit(name='validation', suffix='validation'),  # 推断评估拆分规格
        InferEvalSplit(name='test', suffix='test', include_in_mixture=False)  # 推断评估拆分规格
    ])

# CERBERUS4_CONFIG 是一个 Cerberus4 数据集的配置示例
CERBERUS4_CONFIG = DatasetConfig(
    name='cerberus4',
    paths={
        'train':
            'gs://mt3/data/datasets/cerberus4/slakh_multi_cerberus_train_bass:drums:guitar:piano.tfrecord-?????-of-00286',
        'train_subset':
            'gs://mt3/data/datasets/cerberus4/slakh_multi_cerberus_train_bass:drums:guitar:piano.tfrecord-00000-of-00286',
        'validation':
            'gs://mt3/data/datasets/cerberus4/slakh_multi_cerberus_validation_bass:drums:guitar:piano.tfrecord-?????-of-00212',
        'validation_subset':
            'gs://mt3/data/datasets/cerberus4/slakh_multi_cerberus_validation_bass:drums:guitar:piano.tfrecord-0000?-of-00212',
        'test':
            'gs://mt3/data/datasets/cerberus4/slakh_multi_cerberus_test_bass:drums:guitar:piano.tfrecord-?????-of-00106'
    },
    features={
        'audio_sample_rate': tf.io.FixedLenFeature([], dtype=tf.int64),  # 音频采样率特征
        'inst_names': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.string, allow_missing=True),  # 乐器名称序列特征
        'midi_class': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.int64, allow_missing=True),  # MIDI 类别序列特征
        'mix': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.float32, allow_missing=True),  # 混音序列特征
        'note_sequences': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.string, allow_missing=True),  # 音符序列特征
        'plugin_name': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.int64, allow_missing=True),  # 插件名称序列特征
        'program_num': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.int64, allow_missing=True),  # 程序编号序列特征
        'slakh_class': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.int64, allow_missing=True),  # Slakh 类别序列特征
        'src_ids': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.string, allow_missing=True),  # 源 ID 序列特征
        'stems': tf.io.FixedLenSequenceFeature(
            [], dtype=tf.float32, allow_missing=True),  # 音轨序列特征
        'stems_shape': tf.io.FixedLenFeature([2], dtype=tf.int64),  # 音轨形状特征
        'target_type': tf.io.FixedLenFeature([], dtype=tf.string),  # 目标类型特征
        'track_id': tf.io.FixedLenFeature([], dtype=tf.string),  # 轨道 ID 特征
    },
    train_split='train',  # 训练数据集拆分
    train_eval_split='validation_subset',  # 训练评估拆分
    infer_eval_splits=[
        InferEvalSplit(name='train', suffix='eval_train_full',
                       include_in_mixture=False),  # 推断评估拆分规格
        InferEvalSplit(name='train_subset', suffix='eval_train'),  # 推断评估拆分规格
        InferEvalSplit(name='validation', suffix='validation_full',
                       include_in_mixture=False),  # 推断评估拆分规格
        InferEvalSplit(name='validation_subset', suffix='validation'),  # 推断评估拆分规格
        InferEvalSplit(name='test', suffix='test', include_in_mixture=False)  # 推断评估拆分规格
    ],
    track_specs=[
        note_sequences.TrackSpec('bass', program=32),  # Bass 轨道规格
        note_sequences.TrackSpec('drums', is_drum=True),  # Drums 轨道规格
        note_sequences.TrackSpec('guitar', program=24),  # Guitar 轨道规格
        note_sequences.TrackSpec('piano', program=0)  # Piano 轨道规格
    ])

# SLAKH_CONFIG 是一个 Slakh 数据集的配置示例
SLAKH_CONFIG = DatasetConfig(
    name='slakh',
    paths={
        'train':
            'gs://mt3/data/datasets/slakh/slakh_multi_full_subsets_10_train_all_inst.tfrecord-?????-of-02307',
        'train_subset':
            'gs://mt3/data/datasets/slakh/slakh_multi_full_subsets_10_train_all_inst.tfrecord-00000-of-02307',
        'validation':
            'gs://mt3/data/datasets/slakh/slakh_multi_full_validation_all_inst.tfrecord-?????-of-00168',
        'validation_subset':
            'gs://mt3/data/datasets/slakh/slakh_multi_full_validation_all_inst.tfrecord-0000?-of-00168',
        'test':
            'gs://mt3/data/datasets/slakh/slakh_multi_full_test_all_inst.tfrecord-?????-of-00109'
    },
    features={
        'audio_sample_rate': tf.io.FixedLenFeature([], dtype=tf.int64),  # 音频采样率特征
        'inst_names': tf.io.FixedLenSequenceFeature([], dtype=tf.string,
                                                    allow_missing=True),  # 乐器名称序列特征
        'midi_class': tf.io.FixedLenSequenceFeature([], dtype=tf.int64,
                                                    allow_missing=True),  # MIDI 类别序列特征
        'mix': tf.io.FixedLenSequenceFeature([], dtype=tf.float32,
                                             allow_missing=True),  # 混音序列特征
        'note_sequences': tf.io.FixedLenSequenceFeature([], dtype=tf.string,
                                                        allow_missing=True),  # 音符序列特征
        'plugin_name': tf.io.FixedLenSequenceFeature([], dtype=tf.int64,
                                                     allow_missing=True),  # 插件名称序列特征
        'program_num': tf.io.FixedLenSequenceFeature([], dtype=tf.int64,
                                                     allow_missing=True),  # 程序编号序列特征
        'slakh_class': tf.io.FixedLenSequenceFeature([], dtype=tf.int64,
                                                     allow_missing=True),  # Slakh 类别序列特征
        'src_ids': tf.io.FixedLenSequenceFeature([], dtype=tf.string,
                                                 allow_missing=True),  # 源 ID 序列特征
        'stems': tf.io.FixedLenSequenceFeature([], dtype=tf.float32,
                                               allow_missing=True),  # 音轨序列特征
        'stems_shape': tf.io.FixedLenFeature([2], dtype=tf.int64),  # 音轨形状特征
        'target_type': tf.io.FixedLenFeature([], dtype=tf.string),  # 目标类型特征
        'track_id': tf.io.FixedLenFeature([], dtype=tf.string),  # 轨道 ID 特征
    },
    train_split='train',  # 训练数据集拆分
    train_eval_split='validation_subset',  # 训练评估拆分
    infer_eval_splits=[
        InferEvalSplit(name='train', suffix='eval_train_full',
                       include_in_mixture=False),  # 推断评估拆分规格
        InferEvalSplit(name='train_subset', suffix='eval_train'),  # 推断评估拆分规格
        InferEvalSplit(name='validation', suffix='validation_full',
                       include_in_mixture=False),  # 推断评估拆分规格
        InferEvalSplit(name='validation_subset', suffix='validation'),  # 推断评估拆分规格
        InferEvalSplit(name='test', suffix='test', include_in_mixture=False)  # 推断评估拆分规格
    ])

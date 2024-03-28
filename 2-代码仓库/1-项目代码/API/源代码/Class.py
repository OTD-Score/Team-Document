from IPython.display import display, Audio
import ipywidgets as widgets
import json
import IPython
import functools
import os
import numpy as np
import tensorflow.compat.v2 as tf
import gin
import jax
import librosa
import note_seq
import seqio
import t5
import t5x
from mt3 import metrics_utils
from mt3 import models
from mt3 import network
from mt3 import note_sequences
from mt3 import preprocessors
from mt3 import spectrograms
from mt3 import vocabularies
from google.colab import files
import nest_asyncio
import logging
from datetime import datetime
nest_asyncio.apply()

class InferenceModel(object):
  """T5X 模型的音乐转录包装器。"""

  def __init__(self, checkpoint_path, model_type='mt3'):
    """
    初始化函数。

    参数:
    - checkpoint_path: 模型的检查点路径
    - model_type: 模型类型，可选值为 'ismir2021' 或 'mt3'

    """
    # 模型常量
    if model_type == 'ismir2021':
      num_velocity_bins = 127
      self.encoding_spec = note_sequences.NoteEncodingSpec
      self.inputs_length = 512
    elif model_type == 'mt3':
      num_velocity_bins = 1
      self.encoding_spec = note_sequences.NoteEncodingWithTiesSpec
      self.inputs_length = 256
    else:
      raise ValueError('unknown model_type: %s' % model_type)

    # Gin 文件路径
    gin_files = ['/content/mt3/gin/model.gin',
                 f'/content/mt3/gin/{model_type}.gin']

    # 模型参数
    self.batch_size = 8
    self.outputs_length = 1024
    self.sequence_length = {'inputs': self.inputs_length,
                            'targets': self.outputs_length}

    # PjitPartitioner
    self.partitioner = t5x.partitioning.PjitPartitioner(
        num_partitions=1)

    # 构建 Codecs 和 Vocabularies
    self.spectrogram_config = spectrograms.SpectrogramConfig()
    self.codec = vocabularies.build_codec(
        vocab_config=vocabularies.VocabularyConfig(
            num_velocity_bins=num_velocity_bins))
    self.vocabulary = vocabularies.vocabulary_from_codec(self.codec)
    self.output_features = {
        'inputs': seqio.ContinuousFeature(dtype=tf.float32, rank=2),
        'targets': seqio.Feature(vocabulary=self.vocabulary),
    }

    # 创建 T5X 模型
    self._parse_gin(gin_files)
    self.model = self._load_model()

    # 从检查点恢复
    self.restore_from_checkpoint(checkpoint_path)

  @property
  def input_shapes(self):
    """
    获取输入的形状。

    返回:
    - 输入的形状字典

    """
    return {
          'encoder_input_tokens': (self.batch_size, self.inputs_length),
          'decoder_input_tokens': (self.batch_size, self.outputs_length)
    }

  def _parse_gin(self, gin_files):
    """
    解析用于训练模型的 gin 文件。

    参数:
    - gin_files: 包含 gin 文件路径的列表

    """
    gin_bindings = [
        'from __gin__ import dynamic_registration',
        'from mt3 import vocabularies',
        'VOCAB_CONFIG=@vocabularies.VocabularyConfig()',
        'vocabularies.VocabularyConfig.num_velocity_bins=%NUM_VELOCITY_BINS'
    ]
    with gin.unlock_config():
      gin.parse_config_files_and_bindings(
          gin_files, gin_bindings, finalize_config=False)

  def _load_model(self):
    """
    在解析训练 gin 配置后加载 T5X `Model`。

    返回:
    - T5X `Model` 对象

    """
    model_config = gin.get_configurable(network.T5Config)()
    module = network.Transformer(config=model_config)
    return models.ContinuousInputsEncoderDecoderModel(
        module=module,
        input_vocabulary=self.output_features['inputs'].vocabulary,
        output_vocabulary=self.output_features['targets'].vocabulary,
        optimizer_def=t5x.adafactor.Adafactor(decay_rate=0.8, step_offset=0),
        input_depth=spectrograms.input_depth(self.spectrogram_config))

  def restore_from_checkpoint(self, checkpoint_path):
    """
    从检查点中恢复训练状态，重置 self._predict_fn()。

    参数:
    - checkpoint_path: 模型检查点的路径

    """
    # 初始化训练状态
    train_state_initializer = t5x.utils.TrainStateInitializer(
      optimizer_def=self.model.optimizer_def,
      init_fn=self.model.get_initial_variables,
      input_shapes=self.input_shapes,
      partitioner=self.partitioner)

    # 恢复检查点的配置
    restore_checkpoint_cfg = t5x.utils.RestoreCheckpointConfig(
        path=checkpoint_path, mode='specific', dtype='float32')

    # 获取训练状态的轴
    train_state_axes = train_state_initializer.train_state_axes

    # 重置 self._predict_fn()
    self._predict_fn = self._get_predict_fn(train_state_axes)

    # 从检查点或初始状态恢复训练状态
    self._train_state = train_state_initializer.from_checkpoint_or_scratch(
        [restore_checkpoint_cfg], init_rng=jax.random.PRNGKey(0))

  @functools.lru_cache()
  def _get_predict_fn(self, train_state_axes):
    """
    生成一个用于解码的分区预测函数。

    参数:
    - train_state_axes: 训练状态的轴

    返回:
    - 分区预测函数

    """
    def partial_predict_fn(params, batch, decode_rng):
      return self.model.predict_batch_with_aux(
          params, batch, decoder_params={'decode_rng': None})
    return self.partitioner.partition(
        partial_predict_fn,
        in_axis_resources=(
            train_state_axes.params,
            t5x.partitioning.PartitionSpec('data',), None),
        out_axis_resources=t5x.partitioning.PartitionSpec('data',)
    )

  def predict_tokens(self, batch, seed=0):
    """
    从预处理的数据集批次中预测 tokens。

    参数:
    - batch: 预处理的数据集批次
    - seed: 随机数种子，默认为 0

    返回:
    - 预测的 tokens

    """
    # 调用分区预测函数进行预测
    prediction, _ = self._predict_fn(
        self._train_state.params, batch, jax.random.PRNGKey(seed))
    # 解码预测结果并返回
    return self.vocabulary.decode_tf(prediction).numpy()
  def __call__(self, audio):
    """
    从音频样本推断出音符序列。

    参数:
    - audio: 包含音频样本的 1 维 numpy 数组（16kHz），对于单个示例。

    返回:
    - 转录音频的音符序列。

    """
    # 将音频转换为 TF Dataset
    ds = self.audio_to_dataset(audio)
    # 对数据集进行预处理
    ds = self.preprocess(ds)

    # 将数据集转换为 T5X 模型输入
    model_ds = self.model.FEATURE_CONVERTER_CLS(pack=False)(
        ds, task_feature_lengths=self.sequence_length)
    model_ds = model_ds.batch(self.batch_size)

    # 获取推断结果的 tokens
    inferences = (tokens for batch in model_ds.as_numpy_iterator()
                  for tokens in self.predict_tokens(batch))

    # 处理预测结果
    predictions = []
    for example, tokens in zip(ds.as_numpy_iterator(), inferences):
      predictions.append(self.postprocess(tokens, example))

    # 将事件预测转换为 NoteSequence 对象
    result = metrics_utils.event_predictions_to_ns(
        predictions, codec=self.codec, encoding_spec=self.encoding_spec)
    return result['est_ns']

  def audio_to_dataset(self, audio):
    """
    从输入音频创建包含频谱图的 TF Dataset。

    参数:
    - audio: 输入音频的 1 维 numpy 数组

    返回:
    - 包含频谱图的 TF Dataset

    """
    # 将音频转换为频谱图数据集
    frames, frame_times = self._audio_to_frames(audio)
    return tf.data.Dataset.from_tensors({
        'inputs': frames,
        'input_times': frame_times,
    })

  def _audio_to_frames(self, audio):
    """
    从音频计算频谱图帧。

    参数:
    - audio: 输入音频的 1 维 numpy 数组

    返回:
    - 频谱图帧和对应的时间数组

    """
    # 计算频谱图帧
    frame_size = self.spectrogram_config.hop_width
    padding = [0, frame_size - len(audio) % frame_size]
    audio = np.pad(audio, padding, mode='constant')
    frames = spectrograms.split_audio(audio, self.spectrogram_config)
    num_frames = len(audio) // frame_size
    times = np.arange(num_frames) / self.spectrogram_config.frames_per_second
    return frames, times

  def preprocess(self, ds):
    """
    对数据集进行预处理。

    参数:
    - ds: TF Dataset

    返回:
    - 预处理后的 TF Dataset

    """
    # 预处理链
    pp_chain = [
        functools.partial(
            t5.data.preprocessors.split_tokens_to_inputs_length,
            sequence_length=self.sequence_length,
            output_features=self.output_features,
            feature_key='inputs',
            additional_feature_keys=['input_times']),
        # 在训练时发生缓存
        preprocessors.add_dummy_targets,
        functools.partial(
            preprocessors.compute_spectrograms,
            spectrogram_config=self.spectrogram_config)
    ]
    # 依次应用预处理步骤
    for pp in pp_chain:
      ds = pp(ds)
    return ds

  def postprocess(self, tokens, example):
    """
    后处理函数。

    参数:
    - tokens: 预测的 tokens
    - example: 示例

    返回:
    - 处理后的结果字典

    """
    # 去除 EOS（终止符）之后的 tokens
    tokens = self._trim_eos(tokens)
    start_time = example['input_times'][0]
    # 向下取整到最近的符号标记步长
    start_time -= start_time % (1 / self.codec.steps_per_second)
    return {
        'est_tokens': tokens,
        'start_time': start_time,
        # 内部 MT3 代码期望原始输入，这里未使用
        'raw_inputs': []
    }

  @staticmethod
  def _trim_eos(tokens):
    """
    去除 EOS（终止符）之后的 tokens。

    参数:
    - tokens: tokens 数组

    返回:
    - 去除 EOS 之后的 tokens

    """
    tokens = np.array(tokens, np.int32)
    if vocabularies.DECODED_EOS_ID in tokens:
      tokens = tokens[:np.argmax(tokens == vocabularies.DECODED_EOS_ID)]
    return tokens

class MusicDispose(object):
      
    def __init__(self):
      
      # 定义常量
      self.SAMPLE_RATE = 16000
      self.SF2_PATH = 'SGM-v2.01-Sal-Guit-Bass-V1.3.sf2'
      # 加载 gtag.js
      self.load_gtag()
      # 记录事件，事件名称为 'setupComplete'，详细信息为空字典
      self.log_event('setupComplete', {})
    
    @staticmethod  
    def new_log():        

      # 获取当前时间
      current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
      # 构建日志文件名
      log_filename = f'/root/autodl-tmp/log_{current_time}.log'
      # 配置日志
      logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
      
      return log_filename
        
    #处理 Google Analytics
    def load_gtag(self):
        """Loads gtag.js."""
        # 注意：gtag.js 必须在执行合成的同一单元格中加载。它不会持续跨单元格执行！
        html_code = '''
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-4P250YRJ08"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-4P250YRJ08',
            {'referrer': document.referrer.split('?')[0],
                'anonymize_ip': true,
                'page_title': '',
                'page_referrer': '',
                'cookie_prefix': 'magenta',
                'cookie_domain': 'auto',
                'cookie_expires': 0,
                'cookie_flags': 'SameSite=None;Secure'});
        </script>
        '''
        IPython.display.display(IPython.display.HTML(html_code))

    def log_event(self, event_name, event_details):
        """Log event with name and details dictionary."""
        # 将事件信息记录到本地日志
        logging.info(f'Event Name: {event_name}, Event Details: {event_details}')
        
    # # 定义函数 upload_audio 用于上传音频文件并转换为 samples
    # def upload_audio(self,sample_rate):
    #     # 从用户上传的文件中获取数据
    #     data = list(files.upload().values())
    #     if len(data) > 1:
    #         print('Multiple files uploaded; using only one.')
    #     # 将 WAV 数据转换为 samples
    #     return note_seq.audio_io.wav_data_to_samples_librosa(data[0], sample_rate=sample_rate)
        
    def upload_audio(self, audio_file):
       # 从上传的音频文件中获取数据
       data = audio_file.read()

       # 将 WAV 数据转换为 samples
       return note_seq.audio_io.wav_data_to_samples_librosa(data,sample_rate=self.SAMPLE_RATE)
     
    @staticmethod 
    def remove(url):
      os.system(f'rm  {url}  -f')
      # 关闭日志文件句柄，确保所有日志信息都写入文件
      logging.shutdown()

        



class CMt3(MusicDispose):
    
    def __init__(self,MODEL='mt3'):
      
      # 调用父类的构造函数
      super().__init__()
      
      #@markdown `ismir2021` 模型转录仅钢琴音符，包含音符速度。
      #@markdown `mt3` 模型转录多个同时进行的乐器，但不包含音符速度。
      self.MODEL = MODEL #@param["ismir2021", "mt3"]
      
      # 设置检查点路径
      self.checkpoint_path = f'/content/checkpoints/{self.MODEL}/'

      # 记录事件：模型加载开始
      self.log_event('loadModelStart', {'event_category': self.MODEL})
      # 创建 InferenceModel 实例
      self.inference_model = InferenceModel(self.checkpoint_path, self.MODEL)
      # 记录事件：模型加载完成
      self.log_event('loadModelComplete', {'event_category': self.MODEL})
    
    def convert(self,audio):
      
      # 记录事件：转录开始
      self.log_event('transcribeStart', {
          'event_category': self.MODEL,
          'value': round(len(audio) / self.SAMPLE_RATE)
      })

      # 使用 InferenceModel 进行音频转录
      est_ns = self.inference_model(audio)

      # 记录事件：转录完成
      self.log_event('transcribeComplete', {
          'event_category': self.MODEL,
          'value': round(len(audio) / self.SAMPLE_RATE),
          'numNotes': sum(1 for note in est_ns.notes if not note.is_drum),
          'numDrumNotes': sum(1 for note in est_ns.notes if note.is_drum),
          'numPrograms': len(set(note.program for note in est_ns.notes
                                if not note.is_drum))
      })
      
      return est_ns
      
    def to_midi(self,est_ns,url='/root/autodl-tmp/transcribed.mid'):
      #@title 下载 MIDI 转录

      # 将 NoteSequence 转换为 MIDI 文件
      note_seq.sequence_proto_to_midi_file(est_ns,url)
      # print(est_ns,url)

      
    

class Cspleeter(MusicDispose):
    pass

class CCreate(MusicDispose):
    pass
    
# test1=CMt3()

# # 加载 gtag.js
# test1.load_gtag()

# # 记录事件，事件名称为 'setupComplete'，详细信息为空字典
# test1.log_event('setupComplete', {})
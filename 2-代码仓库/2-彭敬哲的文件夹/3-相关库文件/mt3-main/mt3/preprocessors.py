# 版权 2023 年 MT3 作者。
#
# 根据 Apache 许可证 2.0 版本（以下简称“许可证”）获得许可；
# 您只能在遵守许可证的情况下使用此文件。
# 您可以在以下网址获取许可证的副本：
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# 除非适用法律要求或书面同意，否则根据许可证分发的软件是基于“原样”无任何明示或暗示的担保或条件分发的。
# 有关特定语言的权限和限制，请参阅许可证。
#
# “音乐转录预处理器。”

from typing import Any, Callable, Mapping, Optional, Sequence, Tuple

from absl import logging  # 导入 absl.logging 模块
import gin  # 导入 gin 模块
from immutabledict import immutabledict  # 导入 immutabledict 模块
import librosa  # 导入 librosa 模块

from mt3 import event_codec  # 从 mt3 模块导入 event_codec 模块
from mt3 import note_sequences  # 从 mt3 模块导入 note_sequences 模块
from mt3 import run_length_encoding  # 从 mt3 模块导入 run_length_encoding 模块
from mt3 import spectrograms  # 从 mt3 模块导入 spectrograms 模块
from mt3 import vocabularies  # 从 mt3 模块导入 vocabularies 模块

import note_seq  # 导入 note_seq 模块
import numpy as np  # 导入 numpy 模块
import seqio  # 导入 seqio 模块
import tensorflow as tf  # 导入 tensorflow 模块


def add_unique_id(ds: tf.data.Dataset) -> tf.data.Dataset:
    """在数据集的每个示例中添加唯一整数 ID。"""
    def add_id_field(i, ex):
        ex['unique_id'] = [i]
        return ex
    return ds.enumerate().map(
        add_id_field, num_parallel_calls=tf.data.experimental.AUTOTUNE)


@seqio.map_over_dataset
def pad_notesequence_array(ex):
    """填充 NoteSequence 数组，以便稍后可以“拆分”它们。"""
    ex['sequence'] = tf.pad(tf.expand_dims(ex['sequence'], 0),
                            [[0, len(ex['input_times']) - 1]])
    return ex


@seqio.map_over_dataset
def add_dummy_targets(ex):
    """添加虚拟目标；在评估时，实际上不使用目标。"""
    ex['targets'] = np.array([], dtype=np.int32)
    return ex


def _audio_to_frames(
    samples: Sequence[float],
    spectrogram_config: spectrograms.SpectrogramConfig,
) -> Tuple[Sequence[Sequence[int]], np.ndarray]:
    """将音频样本转换为不重叠的帧和帧时间。"""
    frame_size = spectrogram_config.hop_width
    logging.info('将 %d 个样本填充为 %d 的倍数', len(samples), frame_size)
    samples = np.pad(samples,
                     [0, frame_size - len(samples) % frame_size],
                     mode='constant')

    frames = spectrograms.split_audio(samples, spectrogram_config)

    num_frames = len(samples) // frame_size
    logging.info('将 %d 个样本编码为 %d 个帧（每个帧 %d 个样本）',
                 len(samples), num_frames, frame_size)

    times = np.arange(num_frames) / spectrogram_config.frames_per_second
    return frames, times


def _include_inputs(ds, input_record, fields_to_omit=('audio',)):
    """在数据集记录中包含输入记录中的字段（除了音频）。"""
    def include_inputs_fn(output_record):
        for key in set(input_record.keys()) - set(output_record.keys()):
            output_record[key] = input_record[key]
        for key in fields_to_omit:
            del output_record[key]
        return output_record
    return ds.map(include_inputs_fn,
                  num_parallel_calls=tf.data.experimental.AUTOTUNE)


def tokenize_transcription_example(
    ds: tf.data.Dataset, spectrogram_config: spectrograms.SpectrogramConfig,
    codec: event_codec.Codec, is_training_data: bool,
    onsets_only: bool, include_ties: bool, audio_is_samples: bool,
    id_feature_key: Optional[str] = None
) -> tf.data.Dataset:
    """标记音符转录示例以进行游程长度编码。

    输出包括：
      inputs：音频样本帧，num_frames-by-frame_size
      input_time：每帧的时间戳
      targets：音符相关事件的符号序列
      input_event_start_indices：每个输入索引的目标开始索引
      input_event_end_indices：每个输入索引的目标结束索引

    Args:
      ds: 输入数据集。
      spectrogram_config: 频谱图配置。
      codec: 事件词汇编解码器。
      is_training_data: 未使用。
      onsets_only: 如果为 True，则仅包含起始事件（而不是终止、速度或程序）。
      include_ties: 如果为 True，则还写入包含活动音符的状态事件，
          以支持游程长度编码后的“领带”部分。
      audio_is_samples: 如果为 True，则音频是浮点样本，而不是序列化的 WAV。
      id_feature_key: 如果不为 None，则使用数据集中指定的键字段替换序列 ID。

    Returns:
      具有上述输出的数据集。
    """
    del is_training_data

    if onsets_only and include_ties:
        raise ValueError('当只建模起始时，不支持领带。')

    def tokenize(sequence, audio, sample_rate, example_id=None):
        ns = note_seq.NoteSequence.FromString(sequence)
        note_sequences.validate_note_sequence(ns)

        if example_id is not None:
            ns.id = example_id

        if audio_is_samples:
            samples = audio
            if sample_rate != spectrogram_config.sample_rate:
                samples = librosa.resample(
                    samples, sample_rate, spectrogram_config.sample_rate)
        else:
            samples = note_seq.audio_io.wav_data_to_samples_librosa(
                audio, sample_rate=spectrogram_config.sample_rate)

        logging.info('获取样本 %s::%s，长度为 %d',
                     ns.id, ns.filename, len(samples))

        frames, frame_times = _audio_to_frames(samples, spectrogram_config)

        if onsets_only:
            times, values = note_sequences.note_sequence_to_onsets(ns)
        else:
            ns = note_seq.apply_sustain_control_changes(ns)
            times, values = (
                note_sequences.note_sequence_to_onsets_and_offsets_and_programs(ns))

        # 原始 NoteSequence 可能有很多我们不需要的控制变化；
        # 删除它们。
        del ns.control_changes[:]

        (events, event_start_indices, event_end_indices,
         state_events, state_event_indices) = (
             run_length_encoding.encode_and_index_events(
                 state=note_sequences.NoteEncodingState() if include_ties else None,
                 event_times=times,
                 event_values=values,
                 encode_event_fn=note_sequences.note_event_data_to_events,
                 codec=codec,
                 frame_times=frame_times,
                 encoding_state_to_events_fn=(
                     note_sequences.note_encoding_state_to_events
                     if include_ties else None)))

        yield {
            'inputs': frames,
            'input_times': frame_times,
            'targets': events,
            'input_event_start_indices': event_start_indices,
            'input_event_end_indices': event_end_indices,
            'state_events': state_events,
            'input_state_event_indices': state_event_indices,
            'sequence': ns.SerializeToString()
        }

    def process_record(input_record):
        if audio_is_samples and 'sample_rate' not in input_record:
            raise ValueError('当音频是样本时必须提供采样率。')

        args = [
            input_record['sequence'],
            input_record['audio'],
            input_record['sample_rate'] if 'sample_rate' in input_record else 0
        ]
        if id_feature_key is not None:
            args.append(input_record[id_feature_key])

        ds = tf.data.Dataset.from_generator(
            tokenize,
            output_signature={
                'inputs':
                    tf.TensorSpec(
                        shape=(None, spectrogram_config.hop_width),
                        dtype=tf.float32),
                'input_times':
                    tf.TensorSpec(shape=(None,), dtype=tf.float32),
                'targets':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'input_event_start_indices':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'input_event_end_indices':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'state_events':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'input_state_event_indices':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'sequence':
                    tf.TensorSpec(shape=(), dtype=tf.string)
            },
            args=args)

        ds = _include_inputs(ds, input_record)
        return ds

    tokenized_records = ds.flat_map(process_record)
    return tokenized_records


def tokenize_guitarset_example(
    ds: tf.data.Dataset, spectrogram_config: spectrograms.SpectrogramConfig,
    codec: event_codec.Codec, is_training_data: bool,
    onsets_only: bool, include_ties: bool
) -> tf.data.Dataset:
    """标记 GuitarSet 转录示例。"""
    def _preprocess_example(ex, name):
        assert 'inst_names' not in ex, 'Key `inst_names` is already populated.'
        ex['inst_names'] = [name]
        ex['instrument_sequences'] = [ex.pop('sequence')]
        return ex

    ds = ds.map(
        lambda x: _preprocess_example(x, 'Clean Guitar'),
        num_parallel_calls=tf.data.experimental.AUTOTUNE)
    ds = tokenize_example_with_program_lookup(
        ds,
        spectrogram_config=spectrogram_config,
        codec=codec,
        is_training_data=is_training_data,
        inst_name_to_program_fn=guitarset_instrument_to_program,
        onsets_only=onsets_only,
        include_ties=include_ties,
        id_feature_key='id')
    return ds


def guitarset_instrument_to_program(instrument: str) -> int:
    """GuitarSet 中全部是吉他，返回第一个 MIDI 吉他程序号。"""
    if instrument == 'Clean Guitar':
        return 24
    else:
        raise ValueError('未知的 GuitarSet 乐器：%s' % instrument)


def tokenize_example_with_program_lookup(
    ds: tf.data.Dataset,
    spectrogram_config: spectrograms.SpectrogramConfig,
    codec: event_codec.Codec,
    is_training_data: bool,
    onsets_only: bool,
    include_ties: bool,
    inst_name_to_program_fn: Callable[[str], int],
    id_feature_key: Optional[str] = None
) -> tf.data.Dataset:
    """标记示例，可选地查找和分配程序号。

    这可以用于任何数据集，其中可以使用映射函数将 `inst_names` 特征中的乐器名
    映射到一组程序号。

    Args:
      ds: 输入数据集。
      spectrogram_config: 频谱图配置。
      codec: 事件词汇编解码器。
      is_training_data: 未使用。
      onsets_only: 如果为 True，则仅包含起始事件（而不是终止和速度）。
      include_ties: 如果为 True，则包含领带事件。
      inst_name_to_program_fn: 用于将每个示例的 `inst_names` 特征中的乐器名映射
        到 MIDI 程序号的函数。
      id_feature_key: 如果不为 None，则使用数据集中指定的键字段替换序列 ID。

    Returns:
      具有上述输出的数据集。
    """
    del is_training_data

    def tokenize(sequences, inst_names, audio, example_id=None):
        # 将所有轨道的音符添加到单个 NoteSequence 中。
        ns = note_seq.NoteSequence(ticks_per_quarter=220)
        tracks = [note_seq.NoteSequence.FromString(seq) for seq in sequences]
        assert len(tracks) == len(inst_names)
        for track, inst_name in zip(tracks, inst_names):
            program = inst_name_to_program_fn(
                inst_name.decode())

            # 请注意，URMP 数据中没有弯音；下面的块将在遇到弯音时引发 PitchBendError。
            add_track_to_notesequence(ns, track, program=program, is_drum=False,
                                      ignore_pitch_bends=False)

        note_sequences.assign_instruments(ns)
        note_sequences.validate_note_sequence(ns)

        if example_id is not None:
            ns.id = example_id

        samples = note_seq.audio_io.wav_data_to_samples_librosa(
            audio, sample_rate=spectrogram_config.sample_rate)

        logging.info('获取样本 %s::%s，长度为 %d',
                     ns.id, ns.filename, len(samples))

        frames, frame_times = _audio_to_frames(samples, spectrogram_config)

        if onsets_only:
            times, values = note_sequences.note_sequence_to_onsets(ns)
        else:
            times, values = (
                note_sequences.note_sequence_to_onsets_and_offsets_and_programs(ns))

        # 原始 NoteSequence 可能有很多我们不需要的控制变化；
        # 删除它们。
        del ns.control_changes[:]

        (events, event_start_indices, event_end_indices,
         state_events, state_event_indices) = (
             run_length_encoding.encode_and_index_events(
                 state=note_sequences.NoteEncodingState() if include_ties else None,
                 event_times=times,
                 event_values=values,
                 encode_event_fn=note_sequences.note_event_data_to_events,
                 codec=codec,
                 frame_times=frame_times,
                 encoding_state_to_events_fn=(
                     note_sequences.note_encoding_state_to_events
                     if include_ties else None)))

        yield {
            'inputs': frames,
            'input_times': frame_times,
            'targets': events,
            'input_event_start_indices': event_start_indices,
            'input_event_end_indices': event_end_indices,
            'state_events': state_events,
            'input_state_event_indices': state_event_indices,
            'sequence': ns.SerializeToString()
        }

    def process_record(input_record):
        args = [
            input_record['instrument_sequences'],
            input_record['inst_names'],
            input_record['audio'],
        ]
        if id_feature_key is not None:
            args.append(input_record[id_feature_key])

        ds = tf.data.Dataset.from_generator(
            tokenize,
            output_signature={
                'inputs':
                    tf.TensorSpec(
                        shape=(None, spectrogram_config.hop_width),
                        dtype=tf.float32),
                'input_times':
                    tf.TensorSpec(shape=(None,), dtype=tf.float32),
                'targets':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'input_event_start_indices':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'input_event_end_indices':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'state_events':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'input_state_event_indices':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'sequence':
                    tf.TensorSpec(shape=(), dtype=tf.string)
            },
            args=args)

        ds = _include_inputs(ds, input_record)
        return ds

    tokenized_records = ds.flat_map(process_record)
    return tokenized_records


# 每个 URMP 乐器对应的 MIDI 程序号
_URMP_INSTRUMENT_PROGRAMS = immutabledict({
    'vn': 40,   # 小提琴
    'va': 41,   # 中提琴
    'vc': 42,   # 大提琴
    'db': 43,   # 低音提琴
    'tpt': 56,  # 小号
    'tbn': 57,  # 长号
    'tba': 58,  # 大号
    'hn': 60,   # 法国号
    'sax': 64,  # 萨克斯风
    'ob': 68,   # 双簧管
    'bn': 70,   # 巴松管
    'cl': 71,   # 单簧管
    'fl': 73    # 长笛
})

# Slakh 中每个类别对应的程序号和是否是鼓
_SLAKH_CLASS_PROGRAMS = immutabledict({
    'Acoustic Piano': 0,
    'Electric Piano': 4,
    'Chromatic Percussion': 8,
    'Organ': 16,
    'Acoustic Guitar': 24,
    'Clean Electric Guitar': 26,
    'Distorted Electric Guitar': 29,
    'Acoustic Bass': 32,
    'Electric Bass': 33,
    'Violin': 40,
    'Viola': 41,
    'Cello': 42,
    'Contrabass': 43,
    'Orchestral Harp': 46,
    'Timpani': 47,
    'String Ensemble': 48,
    'Synth Strings': 50,
    'Choir and Voice': 52,
    'Orchestral Hit': 55,
    'Trumpet': 56,
    'Trombone': 57,
    'Tuba': 58,
    'French Horn': 60,
    'Brass Section': 61,
    'Soprano/Alto Sax': 64,
    'Tenor Sax': 66,
    'Baritone Sax': 67,
    'Oboe': 68,
    'English Horn': 69,
    'Bassoon': 70,
    'Clarinet': 71,
    'Pipe': 73,
    'Synth Lead': 80,
    'Synth Pad': 88
})


def urmp_instrument_to_program(urmp_instrument: str) -> int:
    """获取与给定 URMP 乐器代码相关联的程序号。"""
    if urmp_instrument not in _URMP_INSTRUMENT_PROGRAMS:
        raise ValueError('未知的 URMP 乐器：%s' % urmp_instrument)
    return _URMP_INSTRUMENT_PROGRAMS[urmp_instrument]


def slakh_class_to_program_and_is_drum(slakh_class: str) -> Tuple[int, bool]:
    """将 Slakh 类别字符串映射到程序号和指示鼓的布尔值。"""
    if slakh_class == 'Drums':
        return 0, True
    elif slakh_class not in _SLAKH_CLASS_PROGRAMS:
        raise ValueError('未知的 Slakh 类别：%s' % slakh_class)
    else:
        return _SLAKH_CLASS_PROGRAMS[slakh_class], False


class PitchBendError(Exception):
    pass


def add_track_to_notesequence(ns: note_seq.NoteSequence,
                              track: note_seq.NoteSequence,
                              program: int, is_drum: bool,
                              ignore_pitch_bends: bool):
    """将轨道添加到 NoteSequence。"""
    if track.pitch_bends and not ignore_pitch_bends:
        raise PitchBendError
    track_sus = note_seq.apply_sustain_control_changes(track)
    for note in track_sus.notes:
        note.program = program
        note.is_drum = is_drum
        ns.notes.extend([note])
        ns.total_time = max(ns.total_time, note.end_time)


def tokenize_slakh_example(
    ds: tf.data.Dataset,
    spectrogram_config: spectrograms.SpectrogramConfig,
    codec: event_codec.Codec,
    is_training_data: bool,
    onsets_only: bool,
    include_ties: bool,
    track_specs: Optional[Sequence[note_sequences.TrackSpec]],
    ignore_pitch_bends: bool
) -> tf.data.Dataset:
    """标记 Slakh 多轨音符转录示例。"""
    def tokenize(sequences, samples, sample_rate, inst_names, example_id):
        if sample_rate != spectrogram_config.sample_rate:
            samples = librosa.resample(
                samples, sample_rate, spectrogram_config.sample_rate)

        frames, frame_times = _audio_to_frames(samples, spectrogram_config)

        # 将所有轨道的音符添加到单个 NoteSequence 中。
        ns = note_seq.NoteSequence(ticks_per_quarter=220)
        tracks = [note_seq.NoteSequence.FromString(seq) for seq in sequences]
        assert len(tracks) == len(inst_names)
        if track_specs:
            # 期望特定轨道。
            assert len(tracks) == len(track_specs)
            for track, spec, inst_name in zip(tracks, track_specs, inst_names):
                # 确保乐器名称与预期相匹配。
                assert inst_name.decode() == spec.name
                try:
                    add_track_to_notesequence(ns, track,
                                              program=spec.program, is_drum=spec.is_drum,
                                              ignore_pitch_bends=ignore_pitch_bends)
                except PitchBendError:
                    # TODO(iansimon): 是否有一种方法可以计数这些？
                    return
        else:
            for track, inst_name in zip(tracks, inst_names):
                # 乐器名称应该是 Slakh 类别。
                program, is_drum = slakh_class_to_program_and_is_drum(
                    inst_name.decode())
                try:
                    add_track_to_notesequence(ns, track, program=program, is_drum=is_drum,
                                              ignore_pitch_bends=ignore_pitch_bends)
                except PitchBendError:
                    # TODO(iansimon): 是否有一种方法可以计数这些？
                    return

        note_sequences.assign_instruments(ns)
        note_sequences.validate_note_sequence(ns)
        if is_training_data:
            # 在训练中修剪重叠的音符（因为我们的事件词汇不能表示它们），但保留原始的 NoteSequence 供评估使用。
            ns = note_sequences.trim_overlapping_notes(ns)

        ns.id = example_id

        if onsets_only:
            times, values = note_sequences.note_sequence_to_onsets(ns)
        else:
            times, values = (
                note_sequences.note_sequence_to_onsets_and_offsets_and_programs(ns))

        (events, event_start_indices, event_end_indices,
         state_events, state_event_indices) = (
             run_length_encoding.encode_and_index_events(
                 state=note_sequences.NoteEncodingState() if include_ties else None,
                 event_times=times,
                 event_values=values,
                 encode_event_fn=note_sequences.note_event_data_to_events,
                 codec=codec,
                 frame_times=frame_times,
                 encoding_state_to_events_fn=(
                     note_sequences.note_encoding_state_to_events
                     if include_ties else None)))

        yield {
            'inputs': frames,
            'input_times': frame_times,
            'targets': events,
            'input_event_start_indices': event_start_indices,
            'input_event_end_indices': event_end_indices,
            'state_events': state_events,
            'input_state_event_indices': state_event_indices,
            'sequence': ns.SerializeToString()
        }

    def process_record(input_record):
        ds = tf.data.Dataset.from_generator(
            tokenize,
            output_signature={
                'inputs':
                    tf.TensorSpec(
                        shape=(None, spectrogram_config.hop_width),
                        dtype=tf.float32),
                'input_times':
                    tf.TensorSpec(shape=(None,), dtype=tf.float32),
                'targets':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'input_event_start_indices':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'input_event_end_indices':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'state_events':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'input_state_event_indices':
                    tf.TensorSpec(shape=(None,), dtype=tf.int32),
                'sequence':
                    tf.TensorSpec(shape=(), dtype=tf.string)
            },
            args=[
                input_record['note_sequences'], input_record['mix'],
                input_record['audio_sample_rate'], input_record['inst_names'],
                input_record['track_id']
            ])

        ds = _include_inputs(ds, input_record, fields_to_omit=['mix', 'stems'])
        return ds

    tokenized_records = ds.flat_map(process_record)
    return tokenized_records


@seqio.map_over_dataset
def compute_spectrograms(ex, spectrogram_config):
    samples = spectrograms.flatten_frames(ex['inputs'])
    ex['inputs'] = spectrograms.compute_spectrogram(
        samples, spectrogram_config)
    ex['raw_inputs'] = samples
    return ex


def handle_too_long(dataset: tf.data.Dataset,
                    output_features: seqio.preprocessors.OutputFeaturesType,
                    sequence_length: seqio.preprocessors.SequenceLengthType,
                    skip: bool = False) -> tf.data.Dataset:
    """处理序列过长的情况，通过失败或跳过它们来进行处理。"""
    def max_length_for_key(key):
        max_length = sequence_length[key]
        if output_features[key].add_eos:
            max_length -= 1
        return max_length

    if skip:
        # 放弃其中一个特征过长的示例。
        def is_not_too_long(ex):
            return not tf.reduce_any(
                [k in output_features and len(v) > max_length_for_key(k)
                 for k, v in ex.items()])
        dataset = dataset.filter(is_not_too_long)

    def assert_not_too_long(key: str, value: tf.Tensor) -> tf.Tensor:
        if key in output_features:
            max_length = max_length_for_key(key)
            tf.debugging.assert_less_equal(
                tf.shape(value)[0], max_length,
                f'"{key}" 字段的值超过了最大长度')
        return value

    # 断言没有示例的特征超过其最大序列长度。
    return dataset.map(
        lambda ex: {k: assert_not_too_long(k, v) for k, v in ex.items()},
        num_parallel_calls=tf.data.experimental.AUTOTUNE)


@gin.configurable
def map_midi_programs(
    ds: tf.data.Dataset,
    codec: event_codec.Codec,
    granularity_type: str = 'full',
    feature_key: str = 'targets'
) -> Mapping[str, Any]:
    """将 MIDI 程序映射应用于令牌序列。"""
    granularity = vocabularies.PROGRAM_GRANULARITIES[granularity_type]

    def _map_program_tokens(ex):
        ex[feature_key] = granularity.tokens_map_fn(ex[feature_key], codec)
        return ex
    return ds.map(_map_program_tokens,
                  num_parallel_calls=tf.data.experimental.AUTOTUNE)

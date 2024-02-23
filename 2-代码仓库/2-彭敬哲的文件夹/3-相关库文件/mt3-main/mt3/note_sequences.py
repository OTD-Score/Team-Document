# 版权声明
# Apache License, Version 2.0 协议
# 详见 http://www.apache.org/licenses/LICENSE-2.0
# 该代码包含一些操作NoteSequence proto的辅助函数

# 导入必要的库和模块
import dataclasses
import itertools
from typing import MutableMapping, MutableSet, Optional, Sequence, Tuple
from mt3 import event_codec
from mt3 import run_length_encoding
from mt3 import vocabularies
import note_seq

# 默认音符参数
DEFAULT_VELOCITY = 100
DEFAULT_NOTE_DURATION = 0.01

# 由于量化可能导致零长度音符，设置最小持续时间
MIN_NOTE_DURATION = 0.01

# TrackSpec类，用于指定音轨信息
@dataclasses.dataclass
class TrackSpec:
  name: str
  program: int = 0
  is_drum: bool = False

# 从NoteSequence中提取指定音轨信息
def extract_track(ns, program, is_drum):
  track = note_seq.NoteSequence(ticks_per_quarter=220)
  track_notes = [note for note in ns.notes
                 if note.program == program and note.is_drum == is_drum]
  track.notes.extend(track_notes)
  track.total_time = (max(note.end_time for note in track.notes)
                      if track.notes else 0.0)
  return track

# 修剪重叠的音符
def trim_overlapping_notes(ns: note_seq.NoteSequence) -> note_seq.NoteSequence:
  """修剪NoteSequence中的重叠音符，并删除零长度音符。"""
  ns_trimmed = note_seq.NoteSequence()
  ns_trimmed.CopyFrom(ns)
  channels = set((note.pitch, note.program, note.is_drum)
                 for note in ns_trimmed.notes)
  for pitch, program, is_drum in channels:
    notes = [note for note in ns_trimmed.notes if note.pitch == pitch
             and note.program == program and note.is_drum == is_drum]
    sorted_notes = sorted(notes, key=lambda note: note.start_time)
    for i in range(1, len(sorted_notes)):
      if sorted_notes[i - 1].end_time > sorted_notes[i].start_time:
        sorted_notes[i - 1].end_time = sorted_notes[i].start_time
  valid_notes = [note for note in ns_trimmed.notes
                 if note.start_time < note.end_time]
  del ns_trimmed.notes[:]
  ns_trimmed.notes.extend(valid_notes)
  return ns_trimmed

# 为音符分配乐器号
def assign_instruments(ns: note_seq.NoteSequence) -> None:
  """为音符分配乐器号；原地修改NoteSequence。"""
  program_instruments = {}
  for note in ns.notes:
    if note.program not in program_instruments and not note.is_drum:
      num_instruments = len(program_instruments)
      note.instrument = (num_instruments if num_instruments < 9
                         else num_instruments + 1)
      program_instruments[note.program] = note.instrument
    elif note.is_drum:
      note.instrument = 9
    else:
      note.instrument = program_instruments[note.program]

# 验证NoteSequence是否包含有效音符
def validate_note_sequence(ns: note_seq.NoteSequence) -> None:
  """如果NoteSequence包含无效音符，则引发ValueError。"""
  for note in ns.notes:
    if note.start_time >= note.end_time:
      raise ValueError('音符的起始时间大于或等于结束时间：%f >= %f' %
                       (note.start_time, note.end_time))
    if note.velocity == 0:
      raise ValueError('音符的速度为零')

# 将音符数组转换为NoteSequence
def note_arrays_to_note_sequence(
    onset_times: Sequence[float],
    pitches: Sequence[int],
    offset_times: Optional[Sequence[float]] = None,
    velocities: Optional[Sequence[int]] = None,
    programs: Optional[Sequence[int]] = None,
    is_drums: Optional[Sequence[bool]] = None
) -> note_seq.NoteSequence:
  """将音符的起始/结束时间、音高和速度数组转换为NoteSequence。"""
  ns = note_seq.NoteSequence(ticks_per_quarter=220)
  for onset_time, offset_time, pitch, velocity, program, is_drum in itertools.zip_longest(
      onset_times, [] if offset_times is None else offset_times,
      pitches, [] if velocities is None else velocities,
      [] if programs is None else programs,
      [] if is_drums is None else is_drums):
    if offset_time is None:
      offset_time = onset_time + DEFAULT_NOTE_DURATION
    if velocity is None:
      velocity = DEFAULT_VELOCITY
    if program is None:
      program = 0
    if is_drum is None:
      is_drum = False
    ns.notes.add(
        start_time=onset_time,
        end_time=offset_time,
        pitch=pitch,
        velocity=velocity,
        program=program,
        is_drum=is_drum)
    ns.total_time = max(ns.total_time, offset_time)
  assign_instruments(ns)
  return ns

# NoteEventData类，用于表示音符事件的数据
@dataclasses.dataclass
class NoteEventData:
  pitch: int
  velocity: Optional[int] = None
  program: Optional[int] = None
  is_drum: Optional[bool] = None
  instrument: Optional[int] = None

# 将NoteSequence转换为音符的起始时间和音高
def note_sequence_to_onsets(
    ns: note_seq.NoteSequence
) -> Tuple[Sequence[float], Sequence[NoteEventData]]:
  """从NoteSequence proto中提取音符的起始时间和音高。"""
  # 根据音高排序，用作后续稳定排序的比较器
  notes = sorted(ns.notes, key=lambda note: note.pitch)
  return ([note.start_time for note in notes],
          [NoteEventData(pitch=note.pitch) for note in notes])

# 将NoteSequence转换为音符的起始和结束时间以及音高
def note_sequence_to_onsets_and_offsets(
    ns: note_seq.NoteSequence,
) -> Tuple[Sequence[float], Sequence[NoteEventData]]:
  """从NoteSequence proto中提取音符的起始和结束时间以及音高。"""
  # 根据音高和音符类型排序，并将音符的结束时间放在前作为后续稳定排序的比较器
  notes = sorted(ns.notes, key=lambda note: note.pitch)
  times = ([note.end_time for note in notes] +
           [note.start_time for note in notes])
  values = ([NoteEventData(pitch=note.pitch, velocity=0) for note in notes] +
            [NoteEventData(pitch=note.pitch, velocity=note.velocity)
             for note in notes])
  return times, values

# 将NoteSequence转换为音符的起始和结束时间以及音高和程序
def note_sequence_to_onsets_and_offsets_and_programs(
    ns: note_seq.NoteSequence,
) -> Tuple[Sequence[float], Sequence[NoteEventData]]:
  """从NoteSequence proto中提取音符的起始和结束时间以及音高和程序。"""
  # 根据程序、音高和音符类型排序，并将非鼓音符的结束时间放在前作为后续稳定排序的比较器
  notes = sorted(ns.notes,
                 key=lambda note: (note.is_drum, note.program, note.pitch))
  times = ([note.end_time for note in notes if not note.is_drum] +
           [note.start_time for note in notes])
  values = ([NoteEventData(pitch=note.pitch, velocity=0,
                           program=note.program, is_drum=False)
             for note in notes if not note.is_drum] +
            [NoteEventData(pitch=note.pitch, velocity=note.velocity,
                           program=note.program, is_drum=note.is_drum)
             for note in notes])
  return times, values

# NoteEncodingState类，用于音符编码状态，跟踪活动音高
@dataclasses.dataclass
class NoteEncodingState:
  """音符转录的编码状态，跟踪活动音高。"""
  # 用于活动音高和程序的速度区间
  active_pitches: MutableMapping[Tuple[int, int], int] = dataclasses.field(
      default_factory=dict)

# 将音符事件数据转换为一系列事件
def note_event_data_to_events(
    state: Optional[NoteEncodingState],
    value: NoteEventData,
    codec: event_codec.Codec,
) -> Sequence[event_codec.Event]:
  """将音符事件数据转换为一系列事件。"""
  if value.velocity is None:
    # 仅处理音符的起始，没有程序和速度
    return [event_codec.Event('pitch', value.pitch)]
  else:
    num_velocity_bins = vocabularies.num_velocity_bins_from_codec(codec)
    velocity_bin = vocabularies.velocity_to_bin(
        value.velocity, num_velocity_bins)
    if value.program is None:
      # 处理音符的起始、结束和速度，没有程序
      if state is not None:
        state.active_pitches[(value.pitch, 0)] = velocity_bin
      return [event_codec.Event('velocity', velocity_bin),
              event_codec.Event('pitch', value.pitch)]
    else:
      if value.is_drum:
        # 鼓事件使用单独的词汇表
        return [event_codec.Event('velocity', velocity_bin),
                event_codec.Event('drum', value.pitch)]
      else:
        # 处理程序、速度和音符的起始
        if state is not None:
          state.active_pitches[(value.pitch, value.program)] = velocity_bin
        return [event_codec.Event('program', value.program),
                event_codec.Event('velocity', velocity_bin),
                event_codec.Event('pitch', value.pitch)]

# 将音符编码状态转换为一系列事件
def note_encoding_state_to_events(
    state: NoteEncodingState
) -> Sequence[event_codec.Event]:
  """输出活动音符的程序和音符事件，以及最后的连接事件。"""
  events = []
  for pitch, program in sorted(
      state.active_pitches.keys(), key=lambda k: k[::-1]):
    if state.active_pitches[(pitch, program)]:
      events += [event_codec.Event('program', program),
                 event_codec.Event('pitch', pitch)]
  events.append(event_codec.Event('tie', 0))
  return events

# NoteDecodingState类，用于音符解码状态
@dataclasses.dataclass
class NoteDecodingState:
  """音符转录的解码状态。"""
  current_time: float = 0.0
  # 用于后续音符起始事件的速度（用于音符结束事件为零）
  current_velocity: int = DEFAULT_VELOCITY
  # 后续音符起始事件的程序
  current_program: int = 0
  # 活动音符的起始时间和速度
  active_pitches: MutableMapping[Tuple[int, int],
                                 Tuple[float, int]] = dataclasses.field(
                                     default_factory=dict)
  # 要从前一个段继续的音符（带有程序）
  tied_pitches: MutableSet[Tuple[int, int]] = dataclasses.field(
      default_factory=set)
  # 是否在段开头的连接部分
  is_tie_section: bool = False
  # 部分解码的NoteSequence
  note_sequence: note_seq.NoteSequence = dataclasses.field(
      default_factory=lambda: note_seq.NoteSequence(ticks_per_quarter=220))

# 解码音符起始事件
def decode_note_onset_event(
    state: NoteDecodingState,
    time: float,
    event: event_codec.Event,
    codec: event_codec.Codec,
) -> None:
  """处理音符起始事件并更新解码状态。"""
  if event.type == 'pitch':
    state.note_sequence.notes.add(
        start_time=time, end_time=time + DEFAULT_NOTE_DURATION,
        pitch=event.value, velocity=DEFAULT_VELOCITY)
    state.note_sequence.total_time = max(state.note_sequence.total_time,
                                         time + DEFAULT_NOTE_DURATION)
  else:
    raise ValueError('意外的事件类型：%s' % event.type)
def _add_note_to_sequence(
    ns: note_seq.NoteSequence,
    start_time: float, end_time: float, pitch: int, velocity: int,
    program: int = 0, is_drum: bool = False
) -> None:
  end_time = max(end_time, start_time + MIN_NOTE_DURATION)
  ns.notes.add(
      start_time=start_time, end_time=end_time,
      pitch=pitch, velocity=velocity, program=program, is_drum=is_drum)
  ns.total_time = max(ns.total_time, end_time)

def decode_note_event(
    state: NoteDecodingState,
    time: float,
    event: event_codec.Event,
    codec: event_codec.Codec
) -> None:
  """处理音符事件并更新解码状态。"""
  if time < state.current_time:
    raise ValueError('事件时间 < 当前时间, %f < %f' % (
        time, state.current_time))
  state.current_time = time
  if event.type == 'pitch':
    pitch = event.value
    if state.is_tie_section:
      # "tied" pitch
      if (pitch, state.current_program) not in state.active_pitches:
        raise ValueError('连接部分中无效的音高/程序：%d/%d' %
                         (pitch, state.current_program))
      if (pitch, state.current_program) in state.tied_pitches:
        raise ValueError('音高/程序已经连接：%d/%d' %
                         (pitch, state.current_program))
      state.tied_pitches.add((pitch, state.current_program))
    elif state.current_velocity == 0:
      # 音符结束
      if (pitch, state.current_program) not in state.active_pitches:
        raise ValueError('未激活的音高/程序的音符关闭：%d/%d' %
                         (pitch, state.current_program))
      onset_time, onset_velocity = state.active_pitches.pop(
          (pitch, state.current_program))
      _add_note_to_sequence(
          state.note_sequence, start_time=onset_time, end_time=time,
          pitch=pitch, velocity=onset_velocity, program=state.current_program)
    else:
      # 音符起始
      if (pitch, state.current_program) in state.active_pitches:
        # 音高已经激活；这不应该真的发生，但我们会试着通过结束上一个音符并开始新的音符来优雅地处理它。
        onset_time, onset_velocity = state.active_pitches.pop(
            (pitch, state.current_program))
        _add_note_to_sequence(
            state.note_sequence, start_time=onset_time, end_time=time,
            pitch=pitch, velocity=onset_velocity, program=state.current_program)
      state.active_pitches[(pitch, state.current_program)] = (
          time, state.current_velocity)
  elif event.type == 'drum':
    # 鼓音符起始（鼓音符没有结束）
    if state.current_velocity == 0:
      raise ValueError('鼓音符事件的速度不能为零')
    offset_time = time + DEFAULT_NOTE_DURATION
    _add_note_to_sequence(
        state.note_sequence, start_time=time, end_time=offset_time,
        pitch=event.value, velocity=state.current_velocity, is_drum=True)
  elif event.type == 'velocity':
    # 速度变化
    num_velocity_bins = vocabularies.num_velocity_bins_from_codec(codec)
    velocity = vocabularies.bin_to_velocity(event.value, num_velocity_bins)
    state.current_velocity = velocity
  elif event.type == 'program':
    # 程序变化
    state.current_program = event.value
  elif event.type == 'tie':
    # 连接部分的结束；结束未声明为连接的活动音符
    if not state.is_tie_section:
      raise ValueError('不在连接部分时结束连接部分事件')
    for (pitch, program) in list(state.active_pitches.keys()):
      if (pitch, program) not in state.tied_pitches:
        onset_time, onset_velocity = state.active_pitches.pop((pitch, program))
        _add_note_to_sequence(
            state.note_sequence,
            start_time=onset_time, end_time=state.current_time,
            pitch=pitch, velocity=onset_velocity, program=program)
    state.is_tie_section = False
  else:
    raise ValueError('意外的事件类型：%s' % event.type)

def begin_tied_pitches_section(state: NoteDecodingState) -> None:
  """在段开头开始连接部分。"""
  state.tied_pitches = set()
  state.is_tie_section = True

def flush_note_decoding_state(
    state: NoteDecodingState
) -> note_seq.NoteSequence:
  """结束所有活动音符并返回生成的NoteSequence。"""
  for onset_time, _ in state.active_pitches.values():
    state.current_time = max(state.current_time, onset_time + MIN_NOTE_DURATION)
  for (pitch, program) in list(state.active_pitches.keys()):
    onset_time, onset_velocity = state.active_pitches.pop((pitch, program))
    _add_note_to_sequence(
        state.note_sequence, start_time=onset_time, end_time=state.current_time,
        pitch=pitch, velocity=onset_velocity, program=program)
  assign_instruments(state.note_sequence)
  return state.note_sequence

class NoteEncodingSpecType(run_length_encoding.EventEncodingSpec):
  pass

# 仅对音符起始建模的编码规范
NoteOnsetEncodingSpec = NoteEncodingSpecType(
    init_encoding_state_fn=lambda: None,
    encode_event_fn=note_event_data_to_events,
    encoding_state_to_events_fn=None,
    init_decoding_state_fn=NoteDecodingState,
    begin_decoding_segment_fn=lambda state: None,
    decode_event_fn=decode_note_onset_event,
    flush_decoding_state_fn=lambda state: state.note_sequence)

# 对音符起始和结束建模的编码规范
NoteEncodingSpec = NoteEncodingSpecType(
    init_encoding_state_fn=lambda: None,
    encode_event_fn=note_event_data_to_events,
    encoding_state_to_events_fn=None,
    init_decoding_state_fn=NoteDecodingState,
    begin_decoding_segment_fn=lambda state: None,
    decode_event_fn=decode_note_event,
    flush_decoding_state_fn=flush_note_decoding_state)

# 对音符起始和结束建模的编码规范，段开头有一个“连接”部分，其中列出了已激活的音符
NoteEncodingWithTiesSpec = NoteEncodingSpecType(
    init_encoding_state_fn=NoteEncodingState,
    encode_event_fn=note_event_data_to_events,
    encoding_state_to_events_fn=note_encoding_state_to_events,
    init_decoding_state_fn=NoteDecodingState,
    begin_decoding_segment_fn=begin_tied_pitches_section,
    decode_event_fn=decode_note_event,
    flush_decoding_state_fn=flush_note_decoding_state)

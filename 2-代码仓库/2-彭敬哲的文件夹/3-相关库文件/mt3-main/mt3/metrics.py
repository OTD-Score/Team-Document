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

"""转录度量。"""

import collections
import copy
import functools
from typing import Any, Iterable, Mapping, Optional, Sequence

import mir_eval

# 导入 MT3 相关模块
from mt3 import event_codec
from mt3 import metrics_utils
from mt3 import note_sequences
from mt3 import spectrograms
from mt3 import summaries
from mt3 import vocabularies

# 导入额外的音乐理论库
import note_seq
import numpy as np
import seqio

# 带有程序的注意分数
def _program_aware_note_scores(
    ref_ns: note_seq.NoteSequence,
    est_ns: note_seq.NoteSequence,
    granularity_type: str
) -> Mapping[str, float]:
  """考虑了程序的情况下计算音符的精度/召回/F1。

  对于非鼓音轨，使用起始和终止。对于鼓音轨，仅使用起始。
  应用指定粒度类型的 MIDI 程序映射。

  Args:
    ref_ns: 具有地面真实标签的参考 NoteSequence。
    est_ns: 估计的 NoteSequence。
    granularity_type: vocabularies.PROGRAM_GRANULARITIES 字典中的字符串键。

  Returns:
    包含精度、召回和 F1 分数的字典。
  """
  program_map_fn = vocabularies.PROGRAM_GRANULARITIES[
      granularity_type].program_map_fn

  # 深度拷贝参考和估计的 NoteSequence，以免修改原始数据
  ref_ns = copy.deepcopy(ref_ns)
  for note in ref_ns.notes:
    if not note.is_drum:
      note.program = program_map_fn(note.program)

  est_ns = copy.deepcopy(est_ns)
  for note in est_ns.notes:
    if not note.is_drum:
      note.program = program_map_fn(note.program)

  # 获取所有可能的（程序，是否鼓）元组
  program_and_is_drum_tuples = (
      set((note.program, note.is_drum) for note in ref_ns.notes) |
      set((note.program, note.is_drum) for note in est_ns.notes)
  )

  drum_precision_sum = 0.0
  drum_precision_count = 0
  drum_recall_sum = 0.0
  drum_recall_count = 0

  nondrum_precision_sum = 0.0
  nondrum_precision_count = 0
  nondrum_recall_sum = 0.0
  nondrum_recall_count = 0

  for program, is_drum in program_and_is_drum_tuples:
    # 提取特定程序和是否鼓的音轨
    est_track = note_sequences.extract_track(est_ns, program, is_drum)
    ref_track = note_sequences.extract_track(ref_ns, program, is_drum)

    # 将音轨转换为值区间和音高
    est_intervals, est_pitches, unused_est_velocities = (
        note_seq.sequences_lib.sequence_to_valued_intervals(est_track))
    ref_intervals, ref_pitches, unused_ref_velocities = (
        note_seq.sequences_lib.sequence_to_valued_intervals(ref_track))

    # 设置参数用于计算精度、召回和 F1
    args = {
        'ref_intervals': ref_intervals, 'ref_pitches': ref_pitches,
        'est_intervals': est_intervals, 'est_pitches': est_pitches
    }
    if is_drum:
      args['offset_ratio'] = None

    # 计算精度、召回、F1 等
    precision, recall, unused_f_measure, unused_avg_overlap_ratio = (
        mir_eval.transcription.precision_recall_f1_overlap(**args))

    # 根据是否鼓分别累加精度和召回
    if is_drum:
      drum_precision_sum += precision * len(est_intervals)
      drum_precision_count += len(est_intervals)
      drum_recall_sum += recall * len(ref_intervals)
      drum_recall_count += len(ref_intervals)
    else:
      nondrum_precision_sum += precision * len(est_intervals)
      nondrum_precision_count += len(est_intervals)
      nondrum_recall_sum += recall * len(ref_intervals)
      nondrum_recall_count += len(ref_intervals)

  # 计算总体精度和召回
  precision_sum = drum_precision_sum + nondrum_precision_sum
  precision_count = drum_precision_count + nondrum_precision_count
  recall_sum = drum_recall_sum + nondrum_recall_sum
  recall_count = drum_recall_count + nondrum_recall_count

  precision = (precision_sum / precision_count) if precision_count else 0
  recall = (recall_sum / recall_count) if recall_count else 0
  f_measure = mir_eval.util.f_measure(precision, recall)

  # 计算鼓和非鼓的精度、召回和 F1
  drum_precision = ((drum_precision_sum / drum_precision_count)
                    if drum_precision_count else 0)
  drum_recall = ((drum_recall_sum / drum_recall_count)
                 if drum_recall_count else 0)
  drum_f_measure = mir_eval.util.f_measure(drum_precision, drum_recall)

  nondrum_precision = ((nondrum_precision_sum / nondrum_precision_count)
                       if nondrum_precision_count else 0)
  nondrum_recall = ((nondrum_recall_sum / nondrum_recall_count)
                    if nondrum_recall_count else 0)
  nondrum_f_measure = mir_eval.util.f_measure(nondrum_precision, nondrum_recall)

  # 返回计算结果的字典
  return {
      f'起始 + 终止 + 程序精度 ({granularity_type})': precision,
      f'起始 + 终止 + 程序召回 ({granularity_type})': recall,
      f'起始 + 终止 + 程序 F1 ({granularity_type})': f_measure,
      f'鼓起始精度 ({granularity_type})': drum_precision,
      f'鼓起始召回 ({granularity_type})': drum_recall,
      f'鼓起始 F1 ({granularity_type})': drum_f_measure,
      f'非鼓起始 + 终止 + 程序精度 ({granularity_type})':
          nondrum_precision,
      f'非鼓起始 + 终止 + 程序召回 ({granularity_type})':
          nondrum_recall,
      f'非鼓起始 + 终止 + 程序 F1 ({granularity_type})':
          nondrum_f_measure
  }

# 音符起始容忍度扫描
def _note_onset_tolerance_sweep(
    ref_ns: note_seq.NoteSequence, est_ns: note_seq.NoteSequence,
    tolerances: Iterable[float] = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5)
) -> Mapping[str, float]:
  """在容忍度范围内计算音符精度/召回/F1。"""
  est_intervals, est_pitches, unused_est_velocities = (
      note_seq.sequences_lib.sequence_to_valued_intervals(est_ns))
  ref_intervals, ref_pitches, unused_ref_velocities = (
      note_seq.sequences_lib.sequence_to_valued_intervals(ref_ns))

  scores = {}

  for tol in tolerances:
    precision, recall, f_measure, _ = (
        mir_eval.transcription.precision_recall_f1_overlap(
            ref_intervals=ref_intervals, ref_pitches=ref_pitches,
            est_intervals=est_intervals, est_pitches=est_pitches,
            onset_tolerance=tol, offset_min_tolerance=tol))

    scores[f'起始 + 终止精度 ({tol})'] = precision
    scores[f'起始 + 终止召回 ({tol})'] = recall
    scores[f'起始 + 终止 F1 ({tol})'] = f_measure

  # 返回容忍度扫描的计算结果
  return scores

def transcription_metrics(
    targets: Sequence[Mapping[str, Any]],
    predictions: Sequence[Mapping[str, Any]],
    codec: event_codec.Codec,
    spectrogram_config: spectrograms.SpectrogramConfig,
    onsets_only: bool,
    use_ties: bool,
    track_specs: Optional[Sequence[note_sequences.TrackSpec]] = None,
    num_summary_examples: int = 5,
    frame_fps: float = 62.5,
    frame_velocity_threshold: int = 30,
) -> Mapping[str, seqio.metrics.MetricValue]:
  """计算 mir_eval 转录度量。"""
  
  # 检查参数有效性
  if onsets_only and use_ties:
    raise ValueError('Ties not compatible with onset-only transcription.')
  if onsets_only:
    encoding_spec = note_sequences.NoteOnsetEncodingSpec
  elif not use_ties:
    encoding_spec = note_sequences.NoteEncodingSpec
  else:
    encoding_spec = note_sequences.NoteEncodingWithTiesSpec

  # 对于每个完整的示例，第一个目标包含 NoteSequence；按 ID 组织。
  full_targets = {}
  for target in targets:
    if target['ref_ns']:
      full_targets[target['unique_id']] = {'ref_ns': target['ref_ns']}

  # 收集相同 ID 的所有预测，并按时间顺序连接它们，以构建完整长度的预测。
  full_predictions = metrics_utils.combine_predictions_by_id(
      predictions=predictions,
      combine_predictions_fn=functools.partial(
          metrics_utils.event_predictions_to_ns,
          codec=codec,
          encoding_spec=encoding_spec))

  assert sorted(full_targets.keys()) == sorted(full_predictions.keys())

  full_target_prediction_pairs = [
      (full_targets[id], full_predictions[id])
      for id in sorted(full_targets.keys())
  ]

  scores = collections.defaultdict(list)
  all_track_pianorolls = collections.defaultdict(list)
  for target, prediction in full_target_prediction_pairs:
    scores['Invalid events'].append(prediction['est_invalid_events'])
    scores['Dropped events'].append(prediction['est_dropped_events'])

    def remove_drums(ns):
      ns_drumless = note_seq.NoteSequence()
      ns_drumless.CopyFrom(ns)
      del ns_drumless.notes[:]
      ns_drumless.notes.extend([note for note in ns.notes if not note.is_drum])
      return ns_drumless

    est_ns_drumless = remove_drums(prediction['est_ns'])
    ref_ns_drumless = remove_drums(target['ref_ns'])

    # 无论是否有单独的音轨，都为全面的 NoteSequence 减去鼓计算度量。
    est_tracks = [est_ns_drumless]
    ref_tracks = [ref_ns_drumless]
    use_track_offsets = [not onsets_only]
    use_track_velocities = [not onsets_only]
    track_instrument_names = ['']

    if track_specs is not None:
      # 分别为每个音轨计算转录度量。
      for spec in track_specs:
        est_tracks.append(note_sequences.extract_track(
            prediction['est_ns'], spec.program, spec.is_drum))
        ref_tracks.append(note_sequences.extract_track(
            target['ref_ns'], spec.program, spec.is_drum))
        use_track_offsets.append(not onsets_only and not spec.is_drum)
        use_track_velocities.append(not onsets_only)
        track_instrument_names.append(spec.name)

    for est_ns, ref_ns, use_offsets, use_velocities, instrument_name in zip(
        est_tracks, ref_tracks, use_track_offsets, use_track_velocities,
        track_instrument_names):
      track_scores = {}

      est_intervals, est_pitches, est_velocities = (
          note_seq.sequences_lib.sequence_to_valued_intervals(est_ns))

      ref_intervals, ref_pitches, ref_velocities = (
          note_seq.sequences_lib.sequence_to_valued_intervals(ref_ns))

      # 使用仅起始（和音高）计算精度/召回/F1。
      precision, recall, f_measure, avg_overlap_ratio = (
          mir_eval.transcription.precision_recall_f1_overlap(
              ref_intervals=ref_intervals,
              ref_pitches=ref_pitches,
              est_intervals=est_intervals,
              est_pitches=est_pitches,
              offset_ratio=None))
      del avg_overlap_ratio
      track_scores['Onset precision'] = precision
      track_scores['Onset recall'] = recall
      track_scores['Onset F1'] = f_measure

      if use_offsets:
        # 使用起始和终止计算精度/召回/F1。
        precision, recall, f_measure, avg_overlap_ratio = (
            mir_eval.transcription.precision_recall_f1_overlap(
                ref_intervals=ref_intervals,
                ref_pitches=ref_pitches,
                est_intervals=est_intervals,
                est_pitches=est_pitches))
        del avg_overlap_ratio
        track_scores['Onset + offset precision'] = precision
        track_scores['Onset + offset recall'] = recall
        track_scores['Onset + offset F1'] = f_measure

      if use_velocities:
        # 使用起始和速度（无终止）计算精度/召回/F1。
        precision, recall, f_measure, avg_overlap_ratio = (
            mir_eval.transcription_velocity.precision_recall_f1_overlap(
                ref_intervals=ref_intervals,
                ref_pitches=ref_pitches,
                ref_velocities=ref_velocities,
                est_intervals=est_intervals,
                est_pitches=est_pitches,
                est_velocities=est_velocities,
                offset_ratio=None))
        track_scores['Onset + velocity precision'] = precision
        track_scores['Onset + velocity recall'] = recall
        track_scores['Onset + velocity F1'] = f_measure

      if use_offsets and use_velocities:
        # 使用起始、终止和速度计算精度/召回/F1。
        precision, recall, f_measure, avg_overlap_ratio = (
            mir_eval.transcription_velocity.precision_recall_f1_overlap(
                ref_intervals=ref_intervals,
                ref_pitches=ref_pitches,
                ref_velocities=ref_velocities,
                est_intervals=est_intervals,
                est_pitches=est_pitches,
                est_velocities=est_velocities))
        track_scores['Onset + offset + velocity precision'] = precision
        track_scores['Onset + offset + velocity recall'] = recall
        track_scores['Onset + offset + velocity F1'] = f_measure

      # 计算帧度量。
      is_drum = all([n.is_drum for n in ref_ns.notes])
      ref_pr = metrics_utils.get_prettymidi_pianoroll(
          ref_ns, frame_fps, is_drum=is_drum)
      est_pr = metrics_utils.get_prettymidi_pianoroll(
          est_ns, frame_fps, is_drum=is_drum)
      all_track_pianorolls[instrument_name].append((est_pr, ref_pr))
      frame_precision, frame_recall, frame_f1 = metrics_utils.frame_metrics(
          ref_pr, est_pr, velocity_threshold=frame_velocity_threshold)
      track_scores['Frame Precision'] = frame_precision
      track_scores['Frame Recall'] = frame_recall
      track_scores['Frame F1'] = frame_f1

      for metric_name, metric_value in track_scores.items():
        if instrument_name:
          scores[f'{instrument_name}/{metric_name}'].append(metric_value)
        else:
          scores[metric_name].append(metric_value)

    # 添加对所有程序粒度的程序感知的音符度量。
    for granularity_type in vocabularies.PROGRAM_GRANULARITIES:
      for name, score in _program_aware_note_scores(
          target['ref_ns'], prediction['est_ns'],
          granularity_type=granularity_type).items():
        scores[name].append(score)

    # 添加（非程序感知的）在起始/终止容忍度范围内的音符度量。
    for name, score in _note_onset_tolerance_sweep(
        ref_ns=ref_ns_drumless, est_ns=est_ns_drumless).items():
      scores[name].append(score)

  # 计算度量的平均值。
  mean_scores = {k: np.mean(v) for k, v in scores.items()}

  # 创建度量的直方图。
  score_histograms = {'%s (hist)' % k: seqio.metrics.Histogram(np.array(v))
                      for k, v in scores.items()}

  # 选择几个示例进行汇总。
  targets_to_summarize, predictions_to_summarize = zip(
      *full_target_prediction_pairs[:num_summary_examples])

  # 计算音频摘要。
  audio_summaries = summaries.audio_summaries(
      targets=targets_to_summarize,
      predictions=predictions_to_summarize,
      spectrogram_config=spectrogram_config)

  # 计算转录摘要。
  transcription_summaries = summaries.transcription_summaries(
      targets=targets_to_summarize,
      predictions=predictions_to_summarize,
      spectrogram_config=spectrogram_config,
      ns_feature_suffix='ns',
      track_specs=track_specs)

  # 创建要汇总的钢琴卷轴字典。
  pianorolls_to_summarize = {
      k: v[:num_summary_examples] for k, v in all_track_pianorolls.items()
  }

  # 计算 PrettyMIDI 钢琴卷轴的摘要。
  prettymidi_pianoroll_summaries = summaries.prettymidi_pianoroll(
      pianorolls_to_summarize, fps=frame_fps)

  # 返回所有计算的度量和摘要。
  return {
      **mean_scores,
      **score_histograms,
      **audio_summaries,
      **transcription_summaries,
      **prettymidi_pianoroll_summaries,
  }

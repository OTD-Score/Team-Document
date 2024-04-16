from music21 import pitch

# 将Google的Note Sequence中的pitch转换为music21中的Pitch对象
def convert_to_music21_pitch(pitch_value):
    # 使用midiToPitchName函数将MIDI音高转换为音名
    pitch_name = pitch.midiToPitchName(pitch_value)
    # 创建music21中的Pitch对象
    music21_pitch = pitch.Pitch(pitch_name)
    return music21_pitch

# 示例
note_sequence_pitch = 60  # MIDI音高为60
music21_pitch = convert_to_music21_pitch(note_sequence_pitch)
print("Google Note Sequence中的pitch:", note_sequence_pitch)
print("对应的music21中的Pitch对象:", music21_pitch.name)

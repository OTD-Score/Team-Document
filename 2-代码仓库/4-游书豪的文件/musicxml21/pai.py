from music21 import *

# 加载 MIDI 文件
midi_file = converter.parse('./fours.mid')

# 获取拍号信息
time_signatures = midi_file.flat.getElementsByClass(meter.TimeSignature)

# 打印拍号信息
for ts in time_signatures:
    print("Time signature:", ts.ratioString)
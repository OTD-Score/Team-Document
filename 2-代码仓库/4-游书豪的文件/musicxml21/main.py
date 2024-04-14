from music21 import *

# 创建一个Score对象，用于保存谱面
score = stream.Score()

# 创建一个Part对象，表示钢琴左手谱
left_hand_part = stream.Part()
left_hand_part.id = 'left_hand'

# 创建一个Part对象，表示钢琴右手谱
right_hand_part = stream.Part()
right_hand_part.id = 'right_hand'
# 低音谱号
right_hand_part.clef = clef.BassClef()

# 添加音符到左手谱
for i in range(20):
    one_measure = stream.Measure()
    left_hand_notes = ['B4', 'F#5', 'B5', 'F#5']
    for note_name in left_hand_notes:
        one_note = note.Note(note_name)
        one_measure.append(one_note)
    left_hand_part.append(one_measure)


# 添加音符到右手谱
right_hand_notes = ['B3', 'F#4', 'B5', 'F#4']
for note_name in right_hand_notes:
    one_note = note.Note(note_name)
    right_hand_part.append(one_note)


# 将左手和右手谱添加到谱面中
score.insert(0, left_hand_part)
score.insert(0, right_hand_part)

# 显示谱面
score.show()
# 生成MusicXML
# score.write('musicxml', 'output.xml')
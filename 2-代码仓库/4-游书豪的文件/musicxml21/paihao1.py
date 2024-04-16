# 音符数据
notes_data = [
    {"pitch": 47, "velocity": 74, "start_time": 0.02, "end_time": 0.33},  
    {"pitch": 54, "velocity": 84, "start_time": 0.3468, "end_time": 0.49},  
    {"pitch": 59, "velocity": 78, "start_time": 0.67, "end_time": 0.77},  
    {"pitch": 54, "velocity": 82, "start_time": 1.01, "end_time": 1.12},  
    {"pitch": 82, "velocity": 79, "start_time": 1.02, "end_time": 1.14},  
    {"pitch": 91, "velocity": 69, "start_time": 1.34, "end_time": 1.35},  
    {"pitch": 43, "velocity": 78, "start_time": 1.33, "end_time": 1.45},  
    {"pitch": 84, "velocity": 68, "start_time": 1.67, "end_time": 1.68},  
    {"pitch": 50, "velocity": 73, "start_time": 1.67, "end_time": 1.82},  
    {"pitch": 55, "velocity": 82, "start_time": 2.0, "end_time": 2.13},  
    {"pitch": 67, "velocity": 75, "start_time": 2.01, "end_time": 2.13},  
    {"pitch": 98, "velocity": 54, "start_time": 2.36, "end_time": 2.4},  
    {"pitch": 50, "velocity": 74, "start_time": 2.34, "end_time": 2.45},  
    {"pitch": 84, "velocity": 65, "start_time": 2.34, "end_time": 2.67},  
    {"pitch": 100, "velocity": 60, "start_time": 2.68, "end_time": 2.7},  
    {"pitch": 45, "velocity": 71, "start_time": 2.67, "end_time": 2.77},  
    {"pitch": 92, "velocity": 67, "start_time": 3.0, "end_time": 3.03},  
    {"pitch": 98, "velocity": 64, "start_time": 3.01, "end_time": 3.05},  
    {"pitch": 52, "velocity": 76, "start_time": 3.0, "end_time": 3.14},  
    {"pitch": 57, "velocity": 82, "start_time": 3.34, "end_time": 3.5},  
    {"pitch": 69, "velocity": 78, "start_time": 3.35, "end_time": 3.5},  
    {"pitch": 92, "velocity": 68, "start_time": 3.67, "end_time": 3.72},  
    {"pitch": 52, "velocity": 76, "start_time": 3.67, "end_time": 3.82},  
    {"pitch": 80, "velocity": 74, "start_time": 3.66, "end_time": 3.82},  
    {"pitch": 98, "velocity": 64, "start_time": 3.68, "end_time": 3.86},  
    {"pitch": 50, "velocity": 74, "start_time": 4.0, "end_time": 4.33}
]


# 计算每个音符的持续时间
durations = [(note["end_time"] - note["start_time"]) for note in notes_data]

# 寻找持续时间的公约数，作为拍号的分母
common_duration = min(durations)

# 计算拍号的分子，即每个小节的拍数
beats_per_measure = sum(int(note_duration // common_duration) for note_duration in durations)

# 打印结果
print("Beats per measure:", beats_per_measure)
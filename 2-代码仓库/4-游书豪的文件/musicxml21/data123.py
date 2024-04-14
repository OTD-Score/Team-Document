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
  
# 定义一个函数，用来四舍五入start_time到小数点后两位  
def round_start_time(start_time):  
    return round(start_time, 2)  
  
# 遍历列表，调整start_time并计算duration  
for i in range(len(notes_data) - 1):  
    # 获取当前和下一个音符的start_time  
    current_start_time = notes_data[i]['start_time']  
    next_start_time = notes_data[i + 1]['start_time']  
      
    # 如果相邻音符的start_time很接近（即小数点后两位相同），则调整当前音符的start_time  
    if round_start_time(current_start_time) == round_start_time(next_start_time):  
        notes_data[i]['start_time'] = round_start_time(next_start_time)  
      
    # 计算当前音符的duration  
    notes_data[i]['duration'] = notes_data[i]['end_time'] - notes_data[i]['start_time']  
  
# 为最后一个音符计算duration  
notes_data[-1]['duration'] = notes_data[-1]['end_time'] - notes_data[-1]['start_time']  
  
# 打印结果查看调整后的列表  
for note in notes_data:  
    print(note)
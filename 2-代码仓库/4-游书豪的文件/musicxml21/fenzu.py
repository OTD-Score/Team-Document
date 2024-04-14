import itertools  
from collections import defaultdict  
  
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
  
# 计算每个音符的时长  
for note in notes_data:  
    note['duration'] = note['end_time'] - note['start_time']  
  
# 将音符按照开始时间排序  
notes_data.sort(key=lambda note: note['start_time'])  
  
# 检查音符是否同时发生（即重叠）  
def is_overlapping(note1, note2):  
    return note1['start_time'] < note2['end_time'] and note2['start_time'] < note1['end_time']  
  
# 根据规则进行分组  
def group_notes(notes):  
    groups = []  
    current_group = []  
    current_group_time = 0  
      
    for note in notes:  
        # 如果当前音符与前一个音符不重叠，或者当前组为空，则将其添加到当前组  
        if not current_group or not is_overlapping(current_group[-1], note):  
            current_group.append(note)  
            current_group_time += note['duration']  
        else:  
            # 如果当前音符与前一个音符重叠，则不将其计入当前组的总时长  
            pass  
          
        # 检查是否应该开始一个新组  
        if not current_group or current_group_time >= 0.1:  
            groups.append(current_group)  
            current_group = [note] if not is_overlapping(current_group[-1], note) else []  
            current_group_time = note['duration'] if current_group else 0  
      
    # 添加最后一个组（如果有的话）  
    if current_group:  
        groups.append(current_group)  
      
    return groups  
  
# 分组并计算每组时间和  
groups = group_notes(notes_data)  
group_durations = [sum(note['duration'] for note in group) for group in groups]  
  
# 输出结果  
for idx, duration in enumerate(group_durations):  
    print(f"Group {idx + 1} duration: {duration:.2f} seconds")
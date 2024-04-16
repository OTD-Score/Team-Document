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
notes_data.sort(key=lambda x: x['start_time'])

groups = []
group_time_sums = []

for note in notes_data:
    if not groups or note['start_time'] - groups[-1][-1]['start_time'] > 0.02:
        groups.append([note])
        group_time_sums.append(note['end_time'] - note['start_time'])
    else:
        conflict = False
        for i in range(len(groups[-1])):
            if abs(note['start_time'] - groups[-1][i]['start_time']) <= 0.02:
                conflict = True
                if note['end_time'] > groups[-1][i]['end_time']:
                    group_time_sums[-1] -= groups[-1][i]['end_time'] - groups[-1][i]['start_time']
                    groups[-1][i] = note
                    group_time_sums[-1] += note['end_time'] - note['start_time']
                break
        if not conflict:
            groups[-1].append(note)
            group_time_sums[-1] += note['end_time'] - note['start_time']

for i, group in enumerate(groups):
    print(f'Group {i+1}:')
    for note in group:
        print(note)
import re
import json

def pitch_to_note_name(pitch):  
    # 音名列表，从C开始，包含所有的半音  
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']  
      
    # 计算pitch在notes列表中的索引  
    # 由于我们是从0开始计数的，而音名列表是从C开始的，所以需要做一些调整  
    # 我们还需要将pitch值映射到0到11的范围内，因为notes列表只有12个元素  
    index = (pitch % 12)  
    # 返回对应的音名  
    return notes[index] + str(1 + (pitch // 12))  # 添加八度标记，假设每12个pitch值是一个新的八度  

def convert_to_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()

    # 使用正则表达式提取数据
    notes_list = re.findall(r'notes {\s*pitch:\s*(\d+)\s*velocity:\s*(\d+)\s*start_time:\s*([\d.]+)\s*end_time:\s*([\d.]+)\s*}', data)

    # 将提取的数据转换为 JSON 格式
    json_data = []
    for note in notes_list:
        pitch, velocity, start_time, end_time = map(float, note)
        duration = round(end_time - start_time,2)
        if(duration< 0.05):
            continue 
        json_data.append({
            # "pitch": int(pitch),
            "pitches" : pitch_to_note_name(int(pitch)),
            # "velocity": int(velocity),
            "start_time": start_time,
            # "end_time": end_time,
            # "duration": duration
        })

    # 写入到输出文件中
    with open(output_file, 'w') as f:
        json.dump(json_data, f, indent=4)

# 调用函数进行转换
convert_to_json('text.txt', 'output.json')

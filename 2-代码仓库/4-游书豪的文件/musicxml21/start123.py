import numpy as np

# 原始音符弹奏时间
start_times = [
    0.02, 0.34, 0.67, 1.01, 1.02, 1.34, 1.33, 1.67, 1.67, 2.0,
    2.01, 2.36, 2.34, 2.34, 2.68, 2.67, 3.0, 3.01, 3.0, 3.34,
    3.35, 3.67, 3.67, 3.66, 3.68, 4.0
]

# 将几乎同时弹奏的时间调整到一致
adjusted_times = []
previous_time = None
for time in start_times:
    if previous_time is not None and abs(time - previous_time) < 0.04:
        adjusted_times.append(previous_time)
    else:
        adjusted_times.append(time)
        previous_time = time

# 计算音符之间的间隔时间
gaps = np.diff(adjusted_times)

# 找到音符间隔时间的平均值
average_gap = np.mean(gaps)

print("调整后的音符弹奏时间:", adjusted_times)
print("音符间隔时间的平均值:", average_gap)

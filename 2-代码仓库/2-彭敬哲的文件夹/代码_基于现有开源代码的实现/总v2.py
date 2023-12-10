from spleeter.separator import Separator
from music21 import stream, note, midi, metadata
from typing import List
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def picture(audio_path,stem_index):
    # 加载音频文件
    y, sr = librosa.load(audio_path, sr=None)

    # 计算 Constant-Q Transform
    CQT = librosa.amplitude_to_db(np.abs(librosa.cqt(y, sr=sr)), ref=np.max)

    # 绘制频谱图
    librosa.display.specshow(CQT, sr=sr, x_axis='time', y_axis='cqt_note')

    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Spectrogram{stem_index}')
    plt.show()


def separate_and_generate_midi(input_audio_path, output_directory, num_stems):
    # 初始化分离器
    separator = Separator(f'spleeter:{num_stems}stems')

    # 进行乐器分离
    separator.separate_to_file(input_audio_path, output_directory)


    # 分别处理每个轨道
    for stem_index in range(0,num_stems):
        # 读取分离后的音轨
        stem_path = f"{output_directory}stems/stem_{stem_index + 1}.wav"
        
        #画出频谱图
        picture(stem_path,stem_index)
       




# 替换成实际的音频文件路径和输出目录
input_audio_path ='D:\我的文档\听音识谱\资源\盘尼西林 - 再谈记忆.mp3'
output_directory = 'D:/我的文档/听音识谱/代码/总_output/'
num_stems =5

# 调用函数进行处理
separate_and_generate_midi(input_audio_path, output_directory, num_stems)


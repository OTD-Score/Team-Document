import librosa
#import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def charge(audio_path,audio_name,name_list):
    # 加载音频文件
    y, sr = librosa.load(audio_path+audio_name+'.wav', sr=None)

    # 计算 Constant-Q Transform
    CQT = librosa.amplitude_to_db(np.abs(librosa.cqt(y, sr=sr)), ref=np.max)

    # 绘制频谱图
    librosa.display.specshow(CQT, sr=sr, x_axis='time', y_axis='cqt_note')
    if audio_name==name_list[0]:
        plt.colorbar(format='%+2.0f dB')
    plt.title(audio_name)

    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5, forward=True)
    fig.savefig('D:\我的文档\听音识谱\代码/音频处理/'+audio_name, dpi=500)



#定义文件名字
audio_name = 'drums'

# 定义音频文件路径
audio_path = 'D:/我的文档/听音识谱/代码/乐器分离/output/盘尼西林 - 再谈记忆/'

name_list=[
   'bass',
   'drums',
   'other',
   'piano',
   'vocals'
]
for name in name_list:
    audio_name=name
    charge(audio_path,audio_name,name_list)
    print(name+' is done')
#plt.show()

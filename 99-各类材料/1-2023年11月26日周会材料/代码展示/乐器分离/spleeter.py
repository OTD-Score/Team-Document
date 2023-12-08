from spleeter.separator import Separator

# 定义输入音频文件路径和输出目录
input_audio_path ='D:\我的文档\听音识谱\资源\盘尼西林 - 再谈记忆.mp3'
output_directory = 'D:/我的文档/听音识谱/代码/乐器分离/output/'

# 初始化分离器
separator = Separator('spleeter:5stems')

# 进行乐器分离
separator.separate_to_file(input_audio_path, output_directory)

# 输出的分离后的音轨将保存在指定的输出目录中

'''
Separator('spleeter:2stems') 创建了一个乐器分离器，指定为分离出两个音轨（通常是声音和伴奏）。
separator.separate_to_file 方法用于将输入的音频文件分离成不同的音轨，并保存在指定的输出目录中。
请注意，Spleeter 提供了不同的预训练模型，你可以根据需要选择不同的配置。在上述示例中，我选择了 spleeter:2stems，你可以根据你的具体需求选择其他配置。请查阅 Spleeter 文档以获取更多信息
https://github.com/deezer/spleeter
'''
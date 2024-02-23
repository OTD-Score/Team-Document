from flask import Flask, request, send_file,session,jsonify
from MusicDisposeCode import *
from datetime import datetime
import secrets
from datetime import timedelta

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # 生成一个16字节（32字符）的十六进制密钥


@app.route('/')
def export_html():
    # 指定 HTML 文件的路径
    html_file_path = '/content/fileshow.html'

    # 使用 Flask 的 send_file 函数发送 HTML 文件
    return send_file(html_file_path, mimetype='text/html')

@app.route('/mt3', methods=['POST'])
def mt3_convert():
    try:
        logname=MusicDispose.new_log()
        print('新建类')
        ModelClass = CMt3('mt3')
        # 获取音频文件
        print('开始上传')
        audio_file = request.files['file']  
        audio = ModelClass.upload_audio(audio_file)  
        print('开始转换')     
        # 使用你的算法转换音频文件
        est_ns=ModelClass.convert(audio)
        #保存和传输midi文件
        print('开始输出')
        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        midi_file_path=f'/root/autodl-tmp/mt3_{current_time}.mid'
        print(midi_file_path)
        ModelClass.to_midi(est_ns,midi_file_path)
        session['mt3_midi_file_path'] = midi_file_path
        session['mt3_logname'] = logname
        print(session)
        print('搞定')
    except Exception as e:
        return f"Error: {str(e)}"
    
    return jsonify({'success': True, 'message': 'Conversion successful'})
    
@app.route('/mt3/download', methods=['GET'])
def mt3_download():
    session.modified = True
    try:
        # 从 session 中获取 ModelClass 和 midi_file_path
        print('下载')
        midi_file_path = session.get('mt3_midi_file_path')
        # 打印信息
        print(f"midi_file_path: {midi_file_path}")
        # 处理下载逻辑...
        return send_file(midi_file_path, mimetype='audio/midi', as_attachment=True, download_name='output.mid')
    except Exception as e:
        return f"Error: {str(e)}"
    # ModelClass.remove(midi_file_path)
    
    
    
@app.route('/ismir2021', methods=['POST'])
def ismir2021_convert():
    try:
        logname=MusicDispose.new_log()
        print('新建类')
        ModelClass = CMt3('ismir2021')
        # 获取音频文件
        print('开始上传')
        audio_file = request.files['file']  
        audio = ModelClass.upload_audio(audio_file)  
        print('开始转换')     
        # 使用你的算法转换音频文件
        est_ns=ModelClass.convert(audio)
        #保存和传输midi文件
        print('开始输出')
        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        midi_file_path=f'/root/autodl-tmp/ismir2021_{current_time}.mid'
        print(midi_file_path)
        ModelClass.to_midi(est_ns,midi_file_path)
        session['ismir2021_midi_file_path'] = midi_file_path
        session['ismir2021_logname'] = logname
        print(session)
        print('搞定')
    except Exception as e:
        return f"Error: {str(e)}"
    
    return jsonify({'success': True, 'message': 'Conversion successful'})
    
@app.route('/ismir2021/download', methods=['GET'])
def ismir2021_download():
    session.modified = True
    try:
        # 从 session 中获取 ModelClass 和 midi_file_path
        print('下载')
        midi_file_path = session.get('ismir2021_midi_file_path')
        # 打印信息
        print(f"midi_file_path: {midi_file_path}")
        # 处理下载逻辑...
        return send_file(midi_file_path, mimetype='audio/midi', as_attachment=True, download_name='output.mid')
    except Exception as e:
        return f"Error: {str(e)}"
    
    

# 用于处理用户不活跃的请求
@app.route('/inactive', methods=['GET'])
def inactive():
    # 删除文件的逻辑...
    for key, value in session.items():
        print(value)
        MusicDispose.remove(value)
    # midi_file_path = session.get('mt3_midi_file_path')
    # MusicDispose.remove(midi_file_path)
    # MusicDispose.remove('/root/autodl-tmp/*.log')
    os.system('ls /root/autodl-tmp  -ahl  >   dir.txt')
    f=open('dir.txt','+rb',encoding='uft-8')
    dircontent=f.read()
    f.close()
    return jsonify({'status': 'success','dir':dircontent})

# 用于下载日志文件
@app.route('/download/log', methods=['GET'])
def log():
    try:
        log_url=session.get('ismir2021_logname')
        return send_file(log_url, download_name=f"{log_url.split('//')[-1]}")
    finally:
        try:
            log_url=session.get('mt3_logname')
            return send_file(log_url, download_name=f"{log_url.split('//')[-1]}")
        except:
            print('None logfiles')
            

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 在0.0.0.0:5000上运行服务器
# ngrok http --domain=instantly-stirred-gnat.ngrok-free.app 5000
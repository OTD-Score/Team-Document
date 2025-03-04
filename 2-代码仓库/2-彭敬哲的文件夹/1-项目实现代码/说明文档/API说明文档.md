# 音频转 MIDI Flask 应用程序

这是一个使用 Flask 构建的简单 Web 应用程序，用于将音频文件转换为 MIDI 文件。该应用程序支持两个模型：`mt3` 和 `ismir2021`。

域名：[音频转MIDI (instantly-stirred-gnat.ngrok-free.app)](https://instantly-stirred-gnat.ngrok-free.app/)

## API 端点

### 1. `/`

- **方法：** GET

- **描述：** 提供一个 HTML 页面，允许用户上传音频文件并选择模型进行转换。

- **返回：** 返回 HTML 页面。

  

### 2. `/mt3`

- **方法：** POST
- **描述：** 将上传的音频文件使用 `mt3` 模型转换为 MIDI 文件。
- **返回：** JSON 对象，包含转换成功与否的信息、和文件下载地址（格式与/ismir2021返回值类似）。



### 4. `/ismir2021`

- **方法：** POST

- **描述：** 将上传的音频文件使用 `ismir2021` 模型转换为 MIDI 文件。

- **返回：** JSON 对象，包含转换成功与否的信息、和文件下载地址。

  如：

  ```json
  {
      "message": "Conversion successful",
      "midi_file_path": "/root/autodl-tmp/ismir2021_2024-05-29_17-51-27.mid",
      "success": true
  }
  ```

  

### 5. `/download`

- **方法：** GET

- **描述：** 提供下载地址。

  ```json
  https://instantly-stirred-gnat.ngrok-free.app/download?file_path=${encodeURIComponent(filePath)}
  
  例：https://instantly-stirred-gnat.ngrok-free.app/download?file_path=/root/autodl-tmp/ismir2021_2024-05-29_17-51-27.mid
  ```

- **返回：** MIDI 文件。

  

### 6. `/inactive`

- **方法：** GET

- **描述：** 处理用户不活跃请求，删除文件夹中的文件。

- **返回：** JSON 对象，包含删除文件的状态和文件夹内容。

  ```json
  {'status': 'success', 'dir': dircontent}
  ```

  

### 7. `/download/log`

- **方法：** GET

- **描述：** 提供下载模型转换过程中生成的日志文件的端点。

- **返回：** 日志文件。

  

## 注意事项

- 该应用程序在 `0.0.0.0:6006 上运行，可以通过公共 IP 地址访问。
- 该应用程序支持 `mt3` 和 `ismir2021` 两个模型。
- 使用 ngrok 或其他工具将本地服务器映射到公共域名使其对外可访问。
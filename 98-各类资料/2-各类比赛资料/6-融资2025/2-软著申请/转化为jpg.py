import os
import fitz

def pdf_to_jpg(pdf_path, output_folder):
    # 打开 PDF 文件
    pdf_document = fitz.open(pdf_path)
    # 获取 PDF 文件的基本名称（不包含扩展名）
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    # 遍历 PDF 文件的每一页
    for page_number in range(len(pdf_document)):
        # 获取当前页
        page = pdf_document.load_page(page_number)
        # 将页面渲染为图像
        pix = page.get_pixmap()
        # 构建输出图像的文件名
        output_path = os.path.join(output_folder, f"{base_name}_page_{page_number + 1}.jpg")
        # 保存图像为 JPG 格式
        pix.save(output_path)
    # 关闭 PDF 文件
    pdf_document.close()

def convert_all_pdfs():
    # 获取当前目录
    current_directory = os.getcwd()
    # 创建一个名为 'output_images' 的输出文件夹
    output_folder = os.path.join(current_directory, 'output_images')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_directory):
        if filename.endswith('.pdf'):
            # 构建 PDF 文件的完整路径
            pdf_path = os.path.join(current_directory, filename)
            # 调用 pdf_to_jpg 函数进行转换
            pdf_to_jpg(pdf_path, output_folder)

if __name__ == "__main__":
    convert_all_pdfs()
    print("所有 PDF 文件已成功转换为 JPG 图片。")
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os


def convert_images_to_pdf(input_folder, output_file, start_index, end_index):
    # 获取输入文件夹中的图片文件列表
    image_files = [f"{i}.jpg" for i in range(start_index, end_index + 1)]

    # 创建一个PDF文件
    pdf_canvas = canvas.Canvas(output_file, pagesize=letter)

    # 显示进度条
    total_images = len(image_files)
    print(f"开始转换 {total_images} 张图片为 PDF：")

    # 循环遍历图片文件并添加到PDF中
    for index, image_file in enumerate(image_files, start=1):
        image_path = os.path.join(input_folder, image_file)

        # 检查文件是否存在
        if os.path.exists(image_path):
            img = Image.open(image_path)
            pdf_canvas.drawInlineImage(img, 0, 0, width=letter[0], height=letter[1])

            # 为每张图片添加新页面（可选）
            pdf_canvas.showPage()

            # 显示进度
            progress = (index / total_images) * 100
            print(f"已完成 {index}/{total_images} 张图片 ({progress:.2f}%)")
        else:
            print(f"警告：文件 {image_file} 不存在，跳过该文件。")

    # 保存PDF文件
    pdf_canvas.save()

    # 完成时的提示
    print(f"PDF 文件已生成：{output_file}")


if __name__ == "__main__":
    input_folder = "./out"  # 将此路径更改为包含图片的文件夹的路径
    output_file = "output.pdf"  # 将此更改为所需的输出PDF文件的名称
    start_index = 1  # 开始索引
    end_index = 184  # 结束索引

    convert_images_to_pdf(input_folder, output_file, start_index, end_index)

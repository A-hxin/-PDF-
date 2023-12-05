# -PDF-
使用Python程序，将重复的网页链接下载下来

# 图片下载脚本使用文档

这个 Python 脚本用于从指定 URL 下载一系列图片，并保存到本地文件夹。脚本使用了 `requests` 和 `tqdm` 库。

## 使用方法

1. **安装依赖库**

   在运行脚本之前，请确保已经安装了以下 Python 库：

   ```bash
   pip install requests tqdm
配置脚本

打开 download_images.py 文件，根据需要修改以下参数：

python
Copy code
base_url = 'https://file.xinjiaoyu.com/ebook/zip/20231016/yn5f46/files/mobile/'
save_folder = './out'  # 保存图片的文件夹路径
运行脚本

在终端中执行以下命令：

bash
Copy code
python download_images.py
脚本将从指定 URL 下载图片，并保存到本地文件夹。

注意事项
请确保文件夹路径正确设置。
修改 base_url 和 save_folder 以指定下载的图片 URL 和保存的文件夹路径。
示例
bash
Copy code
python download_images.py
这将从指定的 URL 下载图片，并保存到 ./out 文件夹中。

go
Copy code

将上述文本保存为名为 `README.md` 的文件，作为你的使用文档。用户可以通过阅读这个文档来了解脚本的使用方法和注意事项。



---

# 图片转PDF脚本使用文档

这个 Python 脚本用于将指定范围内的图片合并成一个 PDF 文件。脚本使用了 `reportlab` 和 `Pillow` 库。

## 使用方法

1. **安装依赖库**

   在运行脚本之前，请确保已经安装了以下 Python 库：

   ```bash
   pip install reportlab pillow
配置脚本

打开 convert_images_to_pdf.py 文件，根据需要修改以下参数：

python
Copy code
input_folder = "./out"      # 包含图片的文件夹路径
output_file = "output.pdf"  # 输出的 PDF 文件名
start_index = 1              # 图片文件名开始索引
end_index = 184              # 图片文件名结束索引
运行脚本

在终端中执行以下命令：

bash
Copy code
python convert_images_to_pdf.py
脚本将在当前工作目录生成一个包含指定范围内图片的 PDF 文件。

注意事项
请确保文件夹路径和文件名参数正确设置。
如果图片文件不存在，脚本将显示警告并跳过该文件。
修改 start_index 和 end_index 以指定需要转换的图片范围。
示例
bash
Copy code
python convert_images_to_pdf.py
这将转换 ./out 文件夹中 1.jpg 到 184.jpg 的图片为一个名为 output.pdf 的 PDF 文件。

go
Copy code

你可以将上述文本保存为名为 `README.md` 的文件，用作你的使用文档。用户可以通过阅读这个文档来了解脚本的使用方法和注意事项。











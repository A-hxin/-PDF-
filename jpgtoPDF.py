import requests
import os
from tqdm import tqdm


# 文件下载函数
def download_image(url, folder_path, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()

        return file_path
    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")
        return None

# 图片下载的基础URL和保存路径
base_url = 'https://file.xinjiaoyu.com/ebook/zip/20231016/yn5f46/files/mobile/'
save_folder = './out'  # 替换为你想保存的路径

# 创建保存路径
os.makedirs(save_folder, exist_ok=True)

# 下载1.jpg到184.jpg
for i in range(1, 185):
    image_url = f'{base_url}{i}.jpg'
    download_image(image_url, save_folder, f'{i}.jpg')

print('下载完成！')

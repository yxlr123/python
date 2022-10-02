from blind_watermark import WaterMark
import blind_watermark
import os

blind_watermark.bw_notes.close()

"""
这个文件可以给一个文件夹里 .png 或 .jpg 格式的图片批量添加盲水印
"""
path = "/home/python/数字水印/pic/输出"  # 需要提取水印的图片文件夹
z = [m for m in os.listdir(path) if ".png" in str(m) or ".jpg" in str(m) or ".jpeg" in str(m)]  # 获取文件夹下所有文件
bwm1 = WaterMark(password_img=1, password_wm=2858304517)  # 密码配置
for z in z:
    # 提取
    wm_extract = bwm1.extract(f'{path}/{z}', wm_shape=231, mode='str')
    print(f"{z}:{wm_extract}")

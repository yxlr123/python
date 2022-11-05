from blind_watermark import WaterMark
import os
from os import system
import blind_watermark

blind_watermark.bw_notes.close()
system("clear")  # 我有强迫症
"""
这个文件可以给一个文件夹里 .png 或 .jpg 格式的图片批量添加盲水印
"""
path = "/home/python/数字水印/pic"  # 需要添加水印的图片文件夹
wm = '@幽香乐容 https://yxlr.tk'  # 水印的内容
system(f"mkdir {path}/输出")
z = [m for m in os.listdir(path) if "." in str(m)]  # 获取文件夹下所有文件
bwm1 = WaterMark(password_img=1, password_wm=2858304517)  # 密码配置

for z in z:
    print(f"开始压缩{z}")
    if (".jpg" or ".jpeg") in str(z):
        system(f"cd {path} && jpegoptim {z}")  # 压缩.jpg图片
    elif ".png" in str(z):
        system(f"cd {path} && optipng {z}")  # 压缩.png图片
    print("压缩完成，开始添加盲水印")
    # 添加水印
    bwm1.read_img(f'{path}/{z}')
    bwm1.read_wm(wm, mode='str')
    bwm1.embed(f'{path}/输出/已添加_{z}')
    len_wm = len(bwm1.wm_bit)
    print(f"{z}添加水印成功")

    if (".jpg" or ".jpeg") in str(z):
        system(f"cd {path}/输出 && jpegoptim 已添加_{z}")  # 压缩.jpg图片
    elif ".png" in str(z):
        system(f"cd {path}/输出 && optipng 已添加_{z}")  # 压缩.png图片
    lenwm = len_wm
print(f"添加盲水印完成，你的len_wm为{lenwm}")
print("添加盲水印成功")

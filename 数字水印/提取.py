from blind_watermark import WaterMark
import os
from os import system

path = "/home/python/数字水印/pic"  # 需要添加水印的图片文件夹
wm = '@幽香乐容 https://yxlr.tk'  # 水印的内容
system(f"mkdir {path}/输出")
z = [m for m in os.listdir(path) if "." in str(m)]  # 获取文件夹下所有文件

for z in z:
    # 添加水印
    bwm1 = WaterMark(password_img=1, password_wm=2858304517)
    bwm1.read_img(f'{path}/{z}')
    bwm1.read_wm(wm, mode='str')
    bwm1.embed(f'{path}/输出/已添加_{z}')
    len_wm = len(bwm1.wm_bit)

    bwm1 = WaterMark(password_img=1, password_wm=2858304517)
    wm_extract = bwm1.extract(f'{path}/输出/已添加_{z}', wm_shape=len_wm, mode='str')
    if wm_extract == wm:
        print(f"{z}添加水印成功")

    system(f"cd {path}/输出 && jpegoptim 已添加_{z}")  # 压缩图片

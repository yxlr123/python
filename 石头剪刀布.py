# coding=utf-8
import random
Xuanxiang = ["a", "b", "c"]  # 选项列表
NOM = random.choice(Xuanxiang)  # 随机一个选项

# 判断机器人输入情况
if NOM == "a":
    BOT = "石头"
elif NOM == "b":
    BOT = "剪刀"
elif NOM == "c":
    BOT = "布"

# 定义所有可能的结果
GIEGUO_1 = "你输了"
GIEGUO_2 = "你赢了"
GIEGUO_3 = "平局"

# 用户输入
print("     石头剪刀布      ")
print("""
a : 石头
b : 剪刀
c : 布
""")
USER = input("请输入")
while USER not in Xuanxiang:
    print('输入有误，请重新出拳')  # 当用户输入错误，提示错误，重新输入
    USER = input()

# 判断用户输入的结果
if USER == "a":
    USER_A = "石头"
elif USER == "b":
    USER_A = "剪刀"
elif USER == "c":
    USER_A = "布"

# 平局
if NOM == USER:
    GIEGUO = GIEGUO_3

# 玩家获胜
elif (NOM == "a" and USER == "c" ) or (NOM == "b" and USER == "a" ) or (NOM == "c" and USER == "b"):
    GIEGUO = GIEGUO_2

# 机器人获胜
elif (NOM == "a" and USER == "b" ) or (NOM == "b" and USER == "c" ) or (NOM == "c" and USER == "a"):
    GIEGUO = GIEGUO_1
print(f"{USER_A}(你)VS {BOT}(机器人)")  # 输出游戏情况
print(GIEGUO)  # 输出最终结果
exit()  # 退出

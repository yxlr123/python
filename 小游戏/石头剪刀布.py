# coding=utf-8
import random
Xuanxiang = ["a", "b", "c"]  # 选项列表
nom = random.choice(Xuanxiang)  # 随机一个选项

# 判断机器人输入情况
if nom == "a":
    bot = "石头"
elif nom == "b":
    bot = "剪刀"
elif nom == "c":
    bot = "布"

# 定义所有可能的结果
jieguo_1 = "你输了"
jieguo_2 = "你赢了"
jieguo_3 = "平局"

# 用户输入
print("     石头剪刀布      ")
print("""
a : 石头
b : 剪刀
c : 布
""")
user = input("请输入")
while user not in Xuanxiang:
    print('输入有误，请重新出拳')  # 当用户输入错误，提示错误，重新输入
    user = input()

# 判断用户输入的结果
if user == "a":
    user_A = "石头"
elif user == "b":
    user_A = "剪刀"
elif user == "c":
    user_A = "布"

# 平局
if nom == user:
    jieguo = jieguo_3

# 玩家获胜
elif (nom == "a" and user == "c") or (nom == "b" and user == "a") or (nom == "c" and user == "b"):
    jieguo = jieguo_2

# 机器人获胜
elif (nom == "a" and user == "b") or (nom == "b" and user == "c") or (nom == "c" and user == "a"):
    jieguo = jieguo_1
print(f"{user_A}(你)VS {bot}(机器人)")  # 输出游戏情况
print(jieguo)  # 输出最终结果
exit()  # 退出

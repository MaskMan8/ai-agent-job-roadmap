"""用python设计第一个游戏"""


counts=3
while counts > 0:
    temp=input("不妨猜一下小甲鱼现在心里想的是哪个数字:")
    guess=int(temp)
    
    if guess == 8:
        print("你是小甲鱼心里的蛔虫吗？！")
        print("猜中了没奖励")
        break
    else:
        if guess > 8:
            print("大了")
        else:
            print("小了")
    counts=counts-1

print("游戏结束，不玩^_^")



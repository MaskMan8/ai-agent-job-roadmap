import random

counts = int(input("请输入抛硬币的次数"))

print("开始抛硬币实验")

if counts < 100:
    pt = True
else:
    pt = False

heads = 0
tails = 0

i = 1
while i < counts:
    num = random.randint(1,10)
    
    if num % 2:
        heads += 1
        if pt == True:
            print("正面", end=" ")

    else:
        tails += 1
        if pt == True:
            print("反面", end=" ")
            
    i += 1

print(" ")     
print("一共模拟了", counts, "次抛硬币")
print("正面", heads, "次", sep="")
print("反面", tails, "次", sep="")

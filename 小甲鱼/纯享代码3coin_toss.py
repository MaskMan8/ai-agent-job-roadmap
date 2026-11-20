import random

counts = int(input("请输入抛硬币的次数："))

if counts > 100:
    ignore = True
else:
    ignore = False

heads = 0
tails = 0 

last = 0 
c_heads = 0 
c_tails = 0 
max_heads = 0 
max_tails = 0 

i = 0
print("开始抛硬币实验……")
while i < counts:
    num = random.randint(1, 10)

    if num % 2:
        heads += 1
        c_heads += 1

        if not ignore:       
            print("正面", end=" ")

        if last == 2:
            c_heads = 1

        if c_heads > max_heads:
            max_heads = c_heads

        last = 1
    else:
        tails += 1
        c_tails += 1
        
        if not ignore:
            print("反面", end=" ")

        if last == 1:
            c_tails = 1

        if c_tails > max_tails:
            max_tails = c_tails

        last = 2
        
    i += 1

print("")
print("一共模拟了", counts, "次抛硬币，结果如下：")
print("正面：", heads, "次", sep="")
print("反面：", tails, "次", sep="")
print("最多连续正面：", max_heads, "次", sep="")
print("最多连续反面：", max_tails, "次", sep="")

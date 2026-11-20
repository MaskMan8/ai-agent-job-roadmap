import random

counts = int(input("请输入抛硬币的次数："))

# 利用 ignore 变量来判断是否打印每次的结果
if counts > 100:
    ignore = True
else:
    ignore = False

heads = 0 # 统计正面的次数
tails = 0 # 统计反面的次数

last = 0 # 记录上一次的状态，如果是正面设置为1, 反面则设置为2
c_heads = 0 # 统计连续正面的次数
c_tails = 0 # 统计连续反面的次数
max_heads = 0 # 统计连续正面的最多次数
max_tails = 0 # 统计连续反面的最多次数

i = 0
print("开始抛硬币实验……")
while i < counts:
    num = random.randint(1, 10)

# 如果是正面,总计的正面次数加1，连续正面的次数也加1。
    if num % 2:
        heads += 1
        c_heads += 1
"""
如果小于100次就打印
（大于100为True,not ignore为False此条判断不执行也就是不打印，但是如果次数
在100次之内为False，not ignore为True此条判断需要执行也就是打印）
"""
        if not ignore:       
            print("正面", end=" ")

        # *如果上一次是反面：将连续正面的次数设置为1
        if last == 2:
            c_heads = 1

        # 判断连续正面的次数是否比max_heads大，如果是，取而代之
        if c_heads > max_heads:
            max_heads = c_heads

        # 将上一次的状态设置为正面,因为只有将上一次的状态设置为正面才能进行连续正面的累加，也就是不执行*这条语句
        last = 1
    else:
        tails += 1
        c_tails += 1
        
        if not ignore:
            print("反面", end=" ")

        # 如果上一次是正面：连续反面的次数设置为1
        if last == 1:
            c_tails = 1

        # 判断连续反面的次数是否比max_tails大，如果是，取而代之
        if c_tails > max_tails:
            max_tails = c_tails

        # 将上一次的状态设置为反面
        last = 2
        
    i += 1

print("")
print("一共模拟了", counts, "次抛硬币，结果如下：")
print("正面：", heads, "次", sep="")
print("反面：", tails, "次", sep="")
print("最多连续正面：", max_heads, "次", sep="")
print("最多连续反面：", max_tails, "次", sep="")

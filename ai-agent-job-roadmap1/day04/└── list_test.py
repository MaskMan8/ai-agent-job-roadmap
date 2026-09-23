#创建list列表
scores = [20,23,24,25]
#访问元素
print(scores[2])
#修改数据
scores[3] = 29
#添加数据为什么不能写 scores = scores.append(95)？
#因为 append() 的作用是：
#修改原来的列表，而不是创建一个新的列表返回给你。
#要看这个方法是“直接修改原对象”，还是“返回一个新结果”
scores.append(99)
print(scores)
#删除数据
scores.remove(24)
print(scores)
#判断一个数据是否在列表中
if 23 in scores:
    print("23在列表中")
#获取列表长度
print(len(scores))
#排序
scores.sort()
print(scores)




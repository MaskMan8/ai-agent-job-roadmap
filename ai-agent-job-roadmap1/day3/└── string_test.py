#1.测试split:按照指定的内容把字符串分开
text = "PYTHON,SQL,AI,Agent,future"
text = text.split(",")#拆分后的新结果保存到text
print(text)

#2.测试strip去掉字符串两边的空格
text2 = "   Python   "
text2 = text2.strip()
print(text2)

#3.测试replace代替想要代替的字符串
text3 = "我正在学习Python，Python很有趣"
text3 = text3.replace("Python","AI agent")
print(text3)

#4.find() 可以告诉我们“这个内容从哪里开始
text = "Python is useful"
print(text.find("Python"))
print(text.find("useful"))
print(text.find("Java"))

#5.切片的使用；[开始:结束]中是开始和结束的前一个
text4 = "Python"
print(text4[0:2])
print(text4[0:6])
print(text4[2:6])

#6.把变量和文字组合起来输出：字符串前面加f用{}放变量
name = "张三"
major = "数据科学与大数据技术"
target = "AI Agent开发"
print(f"{name}的专业是{major}目标岗位是{target}")
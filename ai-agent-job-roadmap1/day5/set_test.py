skills = {"Python","SQL","Git","Python"}
#打印集合观察Pyhton是否重复
print(skills)
#添加ai
skills.add("ai")
#删除Git
skills.remove("Git")
print(skills)
#判断Python是否存在
if "Python" in skills:
    print("Python in this set")
#输出集合的长度
print(len(skills))

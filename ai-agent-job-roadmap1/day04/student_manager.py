#创建两个列表，一个存放学生的名字，一个存放学生的成绩
names = ["张三", "李四", "王五", "赵六", "小明"]
scores = [80, 90, 92, 90, 88]
#访问元素
print(f"{names[4]}的成绩是{scores[4]}")
#添加数据
names.append(input("请输入你的名字:"))
scores.append(int(input("请输入你的成绩:")))
print("添加后")
print(names,scores)
#删除指定的数据
delete_date= input("输入你要删除的学生数据的名字")
position = names.index(delete_date)
names.pop(position)
scores.pop(position)
print(names,scores)
#按成绩从高到低排序
students = list(zip(names,scores))
key = lambda x: x[1]
new_students = sorted(students,key = key,reverse = True)
print(f"按成绩从高到第依次排序是{new_students}")

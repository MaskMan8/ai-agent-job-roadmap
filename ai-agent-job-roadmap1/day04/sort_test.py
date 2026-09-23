names = ["张三", "李四", "王五"]
scores = [80, 90, 70]

students = list(zip(names, scores))
'''
key=lambda x: x[1]“排序的时候，看每一组数据的第 2 个东西
sorted()返回一个新的排序结果。
'''
key = lambda x: x[1]
new_sort = sorted(students,key = key,reverse = True)
print(new_sort)

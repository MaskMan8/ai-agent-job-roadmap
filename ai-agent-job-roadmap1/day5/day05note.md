'''
dict
一个东西找另一个东西的关系是dict最适合解决的问题
通过key来找value
dict的key是唯一的，value可以重复
list是通过下标来找数据的，dict是通过key来找value的
dict的value可以是任何数据类型，甚至可以是另一个dict。
通过字典中的键来查询数据的两种方式
line["product"]：键不存在时会产生 KeyError。
line.get("product")：键不存在时默认返回 None


set
set是一个无序不重复的元素集合,set中的元素是唯一的,set中的元素是无序的,set中的元素是不可变的。
set是Python中的集合,最大的特点是元素不能重复，
set是无序的,set中的元素是不可变的,唯一的。
list可以重复set可以去重
基本写法
skills = {"ai","wps","java"}
但是set = {}不是空集合，而是一个空的字典
    set()是一个空的集合
1.set.remove()删除集合中的指定元素
2.set.add()添加元素
'''
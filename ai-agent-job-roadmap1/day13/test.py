class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


student1 = Student("张三",24)

print(student1.name,student1.age)
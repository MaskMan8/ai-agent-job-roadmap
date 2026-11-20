

def add_student(students):
    student_id = input("请输入要添加的学生的学号")

    is_duplicate = False

    for student in students:
        if student["id"] == student_id:
            print("已有该学号，添加失败")
            is_duplicate = True
            break
        
    if is_duplicate == False:
        student_name = input("请输入该学生的姓名")
        student = {
            "id": student_id,
            "name": student_name
            }
        students.append(student)
        print("保存成功")
        print(students)


def show_students(students):
    print("将为您查看所有学生")
    if not students:
        print("当前没有学生信息")
    else:
        for student in students:
            print(student["id"],student["name"])



def update_students(students):
    print("请修改学生信息")
    found_id = input("请输入要修改学生信息的id:")
    found = False
    
    for student in students:
        if student["id"] == found_id:
            new_name = input("请输入新的姓名：")
            student["name"] = new_name
            print("修改成功")
            found = True
            break
    if not found:
        print("未找到该学生")  


def delete_student(students, grades):
    student_id = input("请输入要删除学生的学号：")

    # 1. 查找要删除的学生
    for student in students:
        if student["id"] == student_id:

            # 2. 检查该学生是否存在成绩记录
            for grade in grades:
                if grade["student_id"] == student_id:
                    print("该学生存在成绩记录，不能删除！")
                    return

            # 3. 没有关联成绩，允许删除
            students.remove(student)
            print("删除成功！")
            return

    # 4. 遍历结束仍未找到学生
    print("未找到该学生！")



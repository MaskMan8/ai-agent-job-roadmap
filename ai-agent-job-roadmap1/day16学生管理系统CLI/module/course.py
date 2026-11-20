def add_course(courses):
    course_id = input("请输入你要添加的课程id" )
    is_cuplicate = False
    for course in courses:
        if course["id"] == course_id:
            is_cuplicate = True
            print("已有该课程，添加失败")
            break
    if not is_cuplicate:
        course_name = input("请输入要添加的课程名字")
        course = {
            "id": course_id,
            "name": course_name
        }
        courses.append(course)
        print(courses)
        print("添加成功")

def show_courses(courses):
    print("将为您查看所有课程！")
    if not courses:
        print("当前没有课程信息")
    else:
        for course in courses:
            print(course["id"], course["name"])

def update_courses(courses):
    course_id = input("请输入你要修改的课程id:")
    found = False
    for course in courses:
        if course["id"] == course_id:
            course_name = input("请输入你要修改的课程名:")
            course["name"] = course_name
            print("修改成功")
            found = True
            break
    if not found:
        print("没有找到该课程！")


def delete_course(courses, grades):
    course_id = input("请输入要删除的课程ID：")

    # 1. 查找课程是否存在
    for course in courses:
        if course["id"] == course_id:

            # 2. 检查课程是否关联成绩
            for grade in grades:
                if grade["course_id"] == course_id:
                    print("该课程存在成绩记录，不能删除！")
                    return

            # 3. 没有关联成绩，允许删除
            courses.remove(course)
            print("课程删除成功！")
            return

    # 4. 没有找到对应课程
    print("未找到该课程！")



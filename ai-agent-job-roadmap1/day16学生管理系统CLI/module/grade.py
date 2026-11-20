
def add_grade(grades, students, courses):
    # 1. 检查学生是否存在
    add_student_id = input("请输入学生ID：")
    exist_student_id = False

    for student in students:
        if student["id"] == add_student_id:
            exist_student_id = True
            break

    # 2. 检查课程是否存在
    add_course_id = input("请输入课程ID：")
    exist_course_id = False

    for course in courses:
        if course["id"] == add_course_id:
            exist_course_id = True
            break

    # 3. 学生或课程不存在，结束本次添加
    if not exist_student_id or not exist_course_id:
        print("学生或课程不存在，添加失败！")
        return

    # 4. 检查成绩是否重复
    is_duplicate = False

    for grade in grades:
        if (grade["student_id"] == add_student_id
                and grade["course_id"] == add_course_id):
            is_duplicate = True
            break

    if is_duplicate:
        print("该学生的这门课程已有成绩，不能重复添加！")
        return

    # 5. 输入成绩并处理异常
    try:
        score = int(input("请输入学生成绩（0-100）："))
    except ValueError:
        print("请输入有效的整数成绩！")
        return

    # 6. 验证成绩范围
    if not 0 <= score <= 100:
        print("成绩无效，必须在0到100之间！")
        return

    # 7. 创建成绩字典
    grade = {
        "student_id": add_student_id,
        "course_id": add_course_id,
        "score": score
    }

    # 8. 保存成绩
    grades.append(grade)
    print("成绩添加成功！")



def show_grades(grades, students, courses):
    # 1. 检查成绩列表是否为空
    if not grades:
        print("当前没有成绩信息！")
        return

    print("===== 所有学生成绩 =====")

    # 2. 遍历所有成绩
    for grade in grades:
        student_name = "未知学生"
        course_name = "未知课程"

        # 3. 根据学生ID查找学生姓名
        for student in students:
            if student["id"] == grade["student_id"]:
                student_name = student["name"]
                break

        # 4. 根据课程ID查找课程名称
        for course in courses:
            if course["id"] == grade["course_id"]:
                course_name = course["name"]
                break

        # 5. 输出成绩信息
        print(f'学号：{grade["student_id"]}')
        print(f'姓名：{student_name}')
        print(f'课程编号：{grade["course_id"]}')
        print(f'课程名称：{course_name}')
        print(f'成绩：{grade["score"]}')
        print("-------------------------")




def update_grade(grades):
    # 1. 输入要修改的学生ID和课程ID
    student_id = input("请输入要修改成绩的学生ID：")
    course_id = input("请输入要修改成绩的课程ID：")

    found = False

    # 2. 遍历成绩列表
    for grade in grades:
        if grade["student_id"] == student_id and grade["course_id"] == course_id:
            found = True

            # 3. 输入新成绩并处理异常
            try:
                new_score = int(input("请输入新的成绩（0-100）："))
            except ValueError:
                print("请输入有效的整数成绩！")
                return

            # 4. 验证成绩范围
            if not 0 <= new_score <= 100:
                print("成绩无效，必须在0到100之间！")
                return

            # 5. 修改成绩
            grade["score"] = new_score

            print("成绩修改成功！")
            break

    if not found:
        print("未找到该学生的课程成绩！")



def delete_grade(grades):
    # 1. 输入要删除成绩的学生ID和课程ID
    student_id = input("请输入要删除成绩的学生ID：")
    course_id = input("请输入要删除成绩的课程ID：")

    found = False

    # 2. 遍历成绩列表
    for grade in grades:
        if grade["student_id"] == student_id and grade["course_id"] == course_id:

            # 3. 删除找到的成绩
            grades.remove(grade)

            found = True
            print("成绩删除成功！")
            break

    # 4. 没找到时提示
    if not found:
        print("未找到该学生的课程成绩！")

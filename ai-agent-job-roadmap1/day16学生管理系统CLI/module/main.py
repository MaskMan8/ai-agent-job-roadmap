from student import add_student, show_students, update_students, delete_student
from course import add_course, show_courses, update_courses, delete_course
from grade import add_grade, show_grades, update_grade, delete_grade
from storage import save_data, load_data

students, courses, grades = load_data()


while True:
    print("===== 校园信息管理系统 =====")
    print("1. 学生管理")
    print("2. 课程管理")
    print("3. 成绩管理")
    print("4. 退出系统")
    try:
        chosen = int(input("请选择你要执行的操作"))
    except ValueError:
        print("输入错误")
        continue

    if chosen == 1:
        print("进入学生管理")
        while True:
            print("===== 学生管理 =====")
            print("1. 添加学生")
            print("2. 查看所有学生")
            print("3. 修改学生")
            print("4. 删除学生")
            print("5. 返回主菜单")
            try:
                chosen1 = int(input("选择你要执行的操作"))
            except ValueError:
                print("输入错误")
                continue
            if chosen1 == 1:
                add_student(students)
                save_data(students, courses, grades)
            elif chosen1 == 2:
                show_students(students)
            elif chosen1 == 3:
                update_students(students)
                save_data(students, courses, grades)
            elif chosen1 == 4:
                delete_student(students,grades)
                save_data(students, courses, grades)
            elif chosen1 == 5:
                print("即将返回菜单")
                break
            else:
                print("输入无效，请重新输入")
    elif chosen == 2:
        print("进入课程管理")
        while True:
            print("===== 课程管理 =====")
            print("1. 添加课程")
            print("2. 查看所有课程")
            print("3. 修改课程")
            print("4. 删除课程")
            print("5. 返回主菜单")
            try:
                chosen2 = int(input("选择你要执行的操作"))
            except ValueError:
                print("输入错误")
                continue
            if chosen2 == 1:
                add_course(courses)
                save_data(students, courses, grades)
            elif chosen2 == 2:
                show_courses(courses)
            elif chosen2 == 3:
                update_courses(courses)
                save_data(students, courses, grades)
            elif chosen2 == 4:
                delete_course(courses,grades)
                save_data(students, courses, grades)
            elif chosen2 == 5:
                print("即将返回菜单")
                break
            else:
                print("输入无效，请重新输入")
    elif chosen == 3:
        print("进入成绩管理")
        while True:
            print("===== 成绩管理 =====")
            print("1. 添加成绩")
            print("2. 查看所有成绩")
            print("3. 修改成绩")
            print("4. 删除成绩")
            print("5. 返回主菜单")
            try:
                chosen3 = int(input("选择你要执行的操作"))
            except ValueError:
                print("输入错误")
                continue
            if chosen3 == 1:
                add_grade(grades, students, courses)
                save_data(students, courses, grades)
            elif chosen3 == 2:
                show_grades(grades, students, courses)
            elif chosen3 == 3:
                update_grade(grades)
                save_data(students, courses, grades)
            elif chosen3 == 4:
                delete_grade(grades)
                save_data(students, courses, grades)
            elif chosen3 == 5:
                print("返回主菜单！")
                break
            else:
                print("输入无效，请重新输入")
    elif chosen == 4:
        print("退出系统")
        break
    else:
        print("输入无效，请重新输入")


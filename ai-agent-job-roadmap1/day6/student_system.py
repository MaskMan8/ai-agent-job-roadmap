score = []

x = int(input("请输入你的成绩："))

while x != -1:
    score.append(x)
    x = int(input("请输入你的成绩："))

if len(score) == 0:
    print("没有输入有效成绩")

else:
    print(score)

    total = sum(score)
    average = total / len(score)

    print(f"平均分是{average}")
    print(f"最高分是{max(score)}")
    print(f"最低分是{min(score)}")

    pass_people = 0

    for each in score:
        if each >= 60:
            pass_people = pass_people + 1

    pass_rate = pass_people / len(score) * 100

    print(f"及格率是{pass_rate}%")

    for each in score:
        if each >= 90:
            print(f"{each}分：优秀")
        elif each >= 80:
            print(f"{each}分：良好")
        elif each >= 60:
            print(f"{each}分：及格")
        else:
            print(f"{each}分：不及格")
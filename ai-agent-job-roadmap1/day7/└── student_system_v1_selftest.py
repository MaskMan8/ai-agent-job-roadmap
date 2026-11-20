scores = []
score = int(input("请输入成绩"))

while score != -1:
    scores.append(score)
    score = int(input("请输入成绩"))
if score == -1:
    print(f"所有有效成绩是{scores}")

total = sum(scores)
average = total/len(scores)
print(f"平均分是{average}")
print(f"最高成绩是{max(scores)}")
print(f"最低成绩是{min(scores)}")

pass_people = 0
for score in scores:
    if score >= 60:
        pass_people = pass_people + 1
        pass_rate = pass_people/len(scores) * 100
    print(f"及格率是{pass_rate}%")

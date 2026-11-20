name = input("请输入你的名字：")
score1 = int(input("请输入你的成绩1："))
score2 = int(input("请输入你的成绩2："))
score3 = int(input("请输入你的成绩3："))
average = (score1+score2+score3)/3
highest = max(score1,score2,score3)
lowest = min(score1,score2,score3)

print(name,"你的平均成绩是",average,"你的最高成绩是",highest,"你的最低成绩是",lowest)

if average >= 60:
    print("及格")
else:
    print("不及格")
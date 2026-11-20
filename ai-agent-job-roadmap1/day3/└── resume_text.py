#完成下面五个任务
resume = "姓名：张三，专业：数据科学与大数据技术，技能：Python,SQL,Git，目标岗位：AI Agent开发"
# 1. 查找Python在简历中的位置
Python_position = resume.find("Python")
# 2.把Python替换为Python3
new_resume = resume.replace("Python","Python3")
# 3..从简历中截取一部分内容
resume_part = resume[23:38]
# 4.把技能部分拆开
skill = "Python,SQL,Git"
skill_list = skill.split(",")
# 5.输出张三的目标岗位是AI Agent开发，掌握的技能包括Python、SQL、Git。
name = "张三"
major = "AI Agent开发"

print("Python的位置：", Python_position)
print("修改后的简历：", new_resume)
print("简历片段：", resume_part)
print("技能：", skill_list)
print(f"{name}的目标岗位是{major},掌握的技能包括{skill_list}。")

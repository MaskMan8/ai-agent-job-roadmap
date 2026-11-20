# Day 5 通讯录 V1

# 创建通讯录
contacts = {
    "张三": "13800138000",
    "李四": "13900139000",
    "王五": "13700137000"
}

# 1. 查询联系人
name = input("请输入要查询的姓名：")

if name in contacts:
    print(f"{name}的电话号码是：{contacts[name]}")
else:
    print("通讯录中没有这个人")


# 2. 添加联系人
name = input("请输入要添加的姓名：")
phone = input("请输入电话号码：")

contacts[name] = phone

print("添加成功！")
print(contacts)


# 3. 修改联系人
name = input("请输入要修改的姓名：")

if name in contacts:
    phone = input("请输入新的电话号码：")
    contacts[name] = phone
    print("修改成功！")
else:
    print("通讯录中没有这个人")


# 4. 删除联系人
name = input("请输入要删除的姓名：")

if name in contacts:
    del contacts[name]
    print("删除成功！")
else:
    print("通讯录中没有这个人")


# 最终通讯录
print("最终通讯录：")
print(contacts)
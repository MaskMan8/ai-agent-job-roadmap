def login(name,password):
    name = input("请输入你的名字：")
    password = input("请输入你的密码:")
    
    if name == "jack" and password == "1234567":
        print("登录成功")
        return True
    else:
        print("登录失败")
        return False

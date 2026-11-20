#用户功能：暂时只放 login() 登录函数
def login():
    name = input("输入用户名")
    password = input("输入密码")
    
    if name == "k" and password == "12345":
        print("登录成功")
        return True
    else:
        print("用户名或密码错误")
        return False
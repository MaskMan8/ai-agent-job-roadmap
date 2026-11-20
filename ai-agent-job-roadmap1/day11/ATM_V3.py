#读取金额
def load_balance():
    file = None
    try:
        file = open("balance.txt","r")
        content = file.read()
        return int(content)
    except FileNotFoundError:
        print("文件不存在")
        file = open("balance.txt","w")
        file.write(str(1000))
        return 1000
    finally:
        if file is not None:
            file.close()

#保存金额
def save_balance(balance):
    file = None
    try:
        file = open("balance.txt","w")
        file.write(str(balance))
        return True
    except OSError as e:
        print(f"保存失败：{e}")
        return False
    finally:
        if file is not None:
            file.close()


#登录
def login():
    name = input("输入用户名")
    password = input("输入密码")
    
    if name == "k" and password == "12345":
        print("登录成功")
        return True
    else:
        print("用户名或密码错误")
        return False

#查询
def check_balance(balance):
    print(f"您账户的余额是{balance}")

#存款
def deposit(balance, money):
    balance = balance + money
    print(f"存款成功，存款后您账户的余额是{balance}")
    return balance

#取款
def withdraw(balance,money):
    if money > balance:
        print(f"取款失败，您的余额不足{money}")
        return balance
    else:
        balance = balance - money
        print(f"取款成功，取款后您账户的余额是{balance}")
        return balance


#主程序
#启动

balance = load_balance()

#登录
is_login = login()
while is_login == False:
    is_login = login()

while True:
    print("\n===== ATM =====")
    print("1. query balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")
    try:
        chosen = int(input("select the service you want to perform: "))
    except ValueError:
        print("请输入正确的数字")
        continue

    if chosen == 1:
        check_balance(balance)
    elif chosen == 2:
        try:
            money = int(input("输入你要存入的金额："))
        except ValueError:
            print("请输入正确的数字")
            continue
        if money <= 0:
            print("金额无效，返回菜单")
        else:
            balance = deposit(balance, money)
            save_balance(balance)
    elif chosen == 3:
        try:
            money = int(input("输入你要取走的金额："))
        except ValueError:
            print("请输入正确的数字")
            continue
        if money <= 0:
            print("金额无效，返回菜单")
        else:
            balance = withdraw(balance,money)
            save_balance(balance)
    elif chosen == 4:
        break
    else:
        print("输入错误请重新选择：")
    
    
    












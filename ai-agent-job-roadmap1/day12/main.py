#主程序：负责启动 ATM、显示菜单、控制程序流程、调用其他函数。

#1.导入所需模块
from user import login
from utils import load_balance,save_balance,check_balance,deposit,withdraw

#读取余额
balance = load_balance()

#登录
is_login = login()
while is_login == False:
    is_login = login()

#登录成功后进入ATM菜单
while True:
    print("\n===== ATM =====")
    print("1. query balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")
    #选择功能
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
        
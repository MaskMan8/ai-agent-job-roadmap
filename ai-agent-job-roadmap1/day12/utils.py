#功能函数：放置 load_balance()、save_balance()、check_balance()、deposit() 和 withdraw()#读取金额
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


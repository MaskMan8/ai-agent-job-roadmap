#登录
def login():
    name = input("please input your name: ")
    password = input("please input your password: ")

    if name == "w" and password == "321":
        print("login successful!")
        return True
    else:
        print("login failed")
        return False

#查询余额
def check_balance(balance):
    print(f"your balance is {balance}")

#存款
def deposit(balance, money):
    balance = balance + money
    print(f"deposit successful! your balance is {balance}")
    return balance

#取款
def withdraw(balance, money):
    if money > balance:
        print("insufficient balance!")
        return balance
    else:
        balance = balance - money
        print(f"withdraw successful! your balance is {balance}")
        return balance


# 初始余额
balance = 0


# 登录
login_result = login()

while login_result == False:
    print("Re-login")
    login_result = login()


# ATM 主菜单
while True:
    print("\n===== ATM =====")
    print("1. query balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")

    chosen = int(input("select the service you want to perform: "))\

    if chosen == 1:
        check_balance(balance)

    elif chosen == 2:
        money = int(input("input deposit: "))
        balance = deposit(balance, money)

    elif chosen == 3:
        money = int(input("input withdraw: "))
        balance = withdraw(balance, money)

    elif chosen == 4:
        print("exit")
        break

    else:
        print("input error")
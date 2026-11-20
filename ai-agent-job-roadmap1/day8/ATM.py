balance = 1000
while True:
    print("1.查询余额")
    print("2.存款")
    print("3.取款")
    print("4.退出")
    input_ = int(input("请选择你要使用的功能"))
    if input_ == 1:
        print(f"当前余额为{balance}")
    elif input_ == 2:
        bank = int(input("请输入你要存入的金额"))
        balance = balance + bank
        print(f"存款成功，当前余额为:{balance}")
    elif input_ == 3:
        out = int(input("请输入你要取走的金额:"))
        if out > balance:
            print("余额不足")
        else:
            balance = balance - out
            print(f"取款成功，取走了{out}，还剩余{balance}。")
    elif input_ == 4:
        print("退出")
        break
    else:
        print("输入错误")

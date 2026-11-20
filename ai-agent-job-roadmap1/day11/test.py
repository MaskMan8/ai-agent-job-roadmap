
def load_balance():
    file = None

    try:
        file = open("balance.txt", "r")

        content = file.read()

        balance = int(content)

        return balance

    except FileNotFoundError:
        print("余额文件不存在，正在创建新的账户")

        balance = 1000

        file = open("balance.txt", "w")
        file.write(str(balance))

        return balance

    finally:
        if file:
            file.close()
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self,money):
        if money > 0:
            self.balance = self.balance + money
        else:
            print("金额无效")

    def withdraw(self, money):
        if money > 0:
            if money <= self.balance:
                self.balance = self.balance - money
            else:
                print("余额不足")
        else:
            print("金额无效")
        

account1 = Account(1000)
money = int(input("输入存款"))
account1.deposit(money)
money = int(input("输入取款"))
account1.withdraw(money)
print(account1.balance) 




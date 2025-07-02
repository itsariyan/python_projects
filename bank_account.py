class bank_account:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        self.balance-=amount
    def check(self):
        print(f"current balance={self.balance}")

a=bank_account()
a.deposit(1000)
a.withdraw(200)
a.check()

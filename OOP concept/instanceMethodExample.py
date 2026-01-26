import sys
class Bank:
    def __init__(self,name,balance=0.0):
       self.name=name
       self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            print("Balance amount is less.")
        else:
            self.balance-=amount
            
        return self.balance
name="Rupsa"
b=Bank(name)
while(True):
    print("d:Deposit w:withdraw e:exit")
    choice=input("Your choice:")
    if choice=='e'or choice=='E':
        sys.exit()
    amt=float(input("Enter amount:"))
    if choice=='d' or choice=='D':
        print("Balance after deposit",b.deposit(amt))
    elif choice=='w' or choice=='W':
        print("Balance after withdraw",b.withdraw(amt))


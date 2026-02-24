class Deposite :

    acc_amount = 0

    def __init__(self, name : int) :
        self.name = name

    def deposit(self) :
        amount = float(input("Amount : "))
        Deposite.acc_amount += amount
        print(f"\n{self.name}'s Account balance : Rs:{Deposite.acc_amount}\n")

    def balance(self) :
        print(f"Acc Balance : Rs:{Deposite.acc_amount}\n")
import derectory.data_validate as Check
import derectory.Operation as operation

class Deposite :
    check = Check.DataValidation()
    sql = operation.Operation()

    def __init__(self, name : str) :
        self.name = name

    def deposit(self) :
        amount = self.check.CheckIntegers(input("Amount : "))

        #Get returning value from Operation
        acc_balance = self.sql.Income(amount)
        print(f"\n{self.name}'s Account balance : Rs.{acc_balance}\n")

    def expense(self):
        amount = self.check.CheckIntegers(input("Amount : "))

        acc_balance = self.sql.Expenses(amount)
        print(f"{self.name}'s Account balance : Rs.{acc_balance}\n")

    def balance(self) :
        self.sql.GetBalance(self.name)


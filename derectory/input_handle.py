import derectory.data_validate as Check
import derectory.Operation as operation
from derectory import constant

class Deposite :
    check = Check.DataValidation()
    sql = operation.Operation()
    resources = constant.expense_categories

    def __init__(self, name : str) :
        self.name = name

    def deposit(self) :
        amount = self.check.CheckIntegers(input("Amount : ")) #Get amount and check whether it's valid integer

        #Get returning value from Operation
        acc_balance = self.sql.Income(amount)
        print(f"\n{self.name}'s Account balance : Rs.{acc_balance}\n")

    def expense(self):
        amount = self.check.CheckIntegers(input("Amount : "))

        #Display current expenses categories from directory/constant and get category number as the input
        print("\nEnter expenses category ----------------\n")
        for key,value in self.resources.items():
            print(f"{key} : {value}")
        print("\n----------------------------------------\n")
        category_num = input("Enter which category [Category number]: ")

        acc_balance = self.sql.Expenses(amount,self.resources[category_num])
        print(f"\n---------------------------------------------------------\nRs.{amount}.00 is spent for {self.resources[category_num]}")
        print(f"{self.name}'s Account balance : Rs.{acc_balance}\n---------------------------------------------------------\n")

    def balance(self) :
        self.sql.GetBalance(self.name)


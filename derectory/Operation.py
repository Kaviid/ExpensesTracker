import pyodbc
import datetime

class Operation :
  connt = pyodbc.connect(  'Driver={ODBC Driver 17 for SQL Server};' 
                            'Server=.\SQLEXPRESS;'
                            'Database=ExpensesTracker;'
                            'Trusted_Connection=yes;'
                        )
  
  cursor = connt.cursor()

  def __init__(self):
    pass

  def Income(self, amount) :
    quary = "INSERT INTO Statment (TID,date,descreption,income,expenses,balance) VALUES (?,?,?,?,?,?)" #Income add Quary store in var
    date = datetime.datetime.now().date() #Also date store in date var

    #Get current balance and add amount
    self.cursor.execute("SELECT TOP 1 balance FROM Statment ORDER BY TID DESC;") 
    updated_balance = self.cursor.fetchone()[0]
    updated_balance = updated_balance + amount

    #Insert updated values into DataBase
    self.cursor.execute(quary, (12, date, "descreption", amount, None, updated_balance))
    self.connt.commit()
    print("Insert Syccessfully!")

  def Expenses(self, amount) :
    quary = "INSERT INTO Statment (TID, date, descreption, income, expenses, balance) VALUES (?,?,?,?,?,?)" #Expenses add Quary store in var
    date = datetime.datetime.now().date() #Get date

    #Get current balance from the DataBase and substract amount
    self.cursor.execute("SELECT TOP 1 balance FROM Statment ORDER BY TID DESC;")
    updated_balance = self.cursor.fetchone()[0]
    updated_balance = updated_balance - amount

    #Insert 
    self.cursor.execute(quary, (13, date, "Descreption", None, amount, updated_balance))
    self.connt.commit()
    print("Insert Syccessfully!")




test = Operation()
test.Income(4000)
test.Expenses(12000.50)
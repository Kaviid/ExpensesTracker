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
    try :
      quary = "INSERT INTO Statment (date,descreption,income,expenses,balance) VALUES (?,?,?,?,?)" #Income add Quary store in var
      date = datetime.datetime.now().date() #Also date store in date var

      #Get current balance and add amount
      self.cursor.execute("SELECT TOP 1 balance FROM Statment ORDER BY TID DESC;") 
      updated_balance = self.cursor.fetchone()[0]
      updated_balance = updated_balance + amount

      #Insert updated values into DataBase
      self.cursor.execute(quary, (date, "descreption", amount, None, updated_balance))
      self.connt.commit()
      print("Insert Successfully!")

      #Return updated latest balance
      return updated_balance

    except TypeError:
      self.cursor.execute(quary, (date, "descreption", amount, None, amount))
      self.connt.commit()
      print(f"DataBase empty...Added {amount} as the First!")

  def Expenses(self, amount, category) :
    try :
      quary = "INSERT INTO Statment (date, descreption, income, expenses, balance) VALUES (?,?,?,?,?)" #Expenses add Quary store in var
      date = datetime.datetime.now().date() #Get date

      #Get current balance from the DataBase and substract amount
      self.cursor.execute("SELECT TOP 1 balance FROM Statment ORDER BY TID DESC;")
      updated_balance = self.cursor.fetchone()[0]
      updated_balance = updated_balance - amount

      #Insert 
      self.cursor.execute(quary, (date, category, None, amount, updated_balance))
      self.connt.commit()
      #print("Insert Successfully!")

      return updated_balance

    except TypeError: #If thransaction is first value in DB
      self.cursor.execute(quary, (date, category, None, amount, amount))
      self.connt.commit()
      print(f"DataBase empty...Added {amount} as the First!")

  def GetBalance(self, name):
    self.cursor.execute("SELECT TOP 1 balance FROM Statment ORDER BY TID DESC;")
    balance = self.cursor.fetchone()[0]
    print(f"{name}'s current account balance : Rs.{balance}\n")


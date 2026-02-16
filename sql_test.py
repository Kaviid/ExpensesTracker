import pyodbc
 
connt = pyodbc.connect(  'Driver={ODBC Driver 17 for SQL Server};' 
                            'Server=.\SQLEXPRESS;'
                            'Database=ExpensesTracker;'
                            'Trusted_Connection=yes;'
                        )

print("Connected successfully")

cursor = connt.execute("SELECT name FROM sys.tables") # This show all tables in My DB

row = cursor.fetchone() 
print(row) 


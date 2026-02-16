import pyodbc
 
connt = pyodbc.connect(  'Driver={ODBC Driver 17 for SQL Server};' 
                            'Server=.\SQLEXPRESS;'
                            'Database=ExpensesTracker;'
                            'Trusted_Connection=yes;'
                        )

print("Connected successfully")

cursor = connt.execute("SELECT 1")

row = cursor.fetchone() 
print(row) 


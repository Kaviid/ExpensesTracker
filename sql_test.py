import pyodbc
 
connt = pyodbc.connect(  'Driver={ODBC Driver 17 for SQL Server};' 
                            'Server=.\SQLEXPRESS;'
                            'Database=ExpensesTracker;'
                            'Trusted_Connection=yes;'
                        )

cursor = connt.cursor()

quary = "INSERT INTO Statment (date, descreption, income, expenses, balance) VALUES(?,?,?,?,?)"
cursor.execute(quary, ('2026-02-12', 'kaveesha', 23000, None, 400000))

connt.commit()
print("Insert successfully!")

cursor.close()
connt.close()

import pyodbc

connt = pyodbc.Connection(  'Driver={ODBC Driver 17 for SQL Server};'
                            'Server=.\SQLEXPRESS;'
                            'Database=ExpensesTracker;'
                            'Trusted_Connection=yes;'
                        )

print("Connected successfully")

from turtle import clear
import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=GWTN141-10;"
    "Database=AdventureWorks2019;"
    "Trust_Connection=yes;"
)

class sqljson:
    cursor = conn.cursor()
    def __init__(self, connectdb):
        self.connectdb = connectdb 

    def betweenqry(self):
        print("Between Query")
        sqljson.cursor.execute("SELECT top 5 SalesOrderID, OrderDate, DueDate FROM Sales.SalesOrderHeader WHERE [OrderDate] BETWEEN '4/16/2011' AND '12/15/2011'")
        for row in sqljson.cursor:
            print(row)
        print()
      
obj1 = sqljson("converter")
obj1.betweenqry()






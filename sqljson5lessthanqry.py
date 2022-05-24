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
  
    def lessthanqry(conn):
        print("Between Query")
        sqljson.cursor.execute("SELECT BusinessEntityID, FirstName, LastName FROM [Person].[Person] WHERE BusinessEntityID <= 10")
        for row in sqljson.cursor:
            print(row)
        print()
      
obj1 = sqljson("converter")

obj1.lessthanqry()
    
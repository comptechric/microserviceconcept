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

    def read(self):
        print("Read")
        sqljson.cursor.execute("select top 3 BusinessEntityID, FirstName, MiddleName, LastName from [Person].[Person]")
        for row in sqljson.cursor:
            print(row)
        print()

  
      
obj1 = sqljson("converter")
obj1.read()
   




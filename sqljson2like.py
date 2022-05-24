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

    def likeqry(self):
        print("Like Query")
        sqljson.cursor.execute("SELECT top 5 [BusinessEntityID], [JobTitle] FROM [HumanResources].[Employee] e WHERE JobTitle LIKE 'Design%'")
        for row in sqljson.cursor:
            print(row)
        print()
    
      
obj1 = sqljson("converter")
obj1.likeqry()





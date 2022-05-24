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
    
    def INqry(self):
        print("In Query")
        sqljson.cursor.execute("SELECT top 5 [BusinessEntityID],JobTitle FROM [HumanResources].[Employee] e WHERE JobTitle in ('Engineering Manager','Senior Tool Designer')")
        for row in sqljson.cursor:
            print(row)
        print()

obj1 = sqljson("converter")
obj1.INqry()
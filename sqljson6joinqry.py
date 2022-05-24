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

    def joinqry(conn):
        print("Join Tables")
        sqljson.cursor.execute("SELECT top 5 E.NationalIDNumber,   E.JobTitle,   P.FirstName,   P.LastName FROM [HumanResources].[Employee] as E INNER JOIN [Person].[Person] as P on E.BusinessEntityID = P.BusinessEntityID")
        for row in sqljson.cursor:
            print(row)
        print()
    
obj1 = sqljson("converter")

obj1.joinqry()






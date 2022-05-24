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

    
    def queryjson(self):
        print("Query Json Data")
        sqljson.cursor.execute('''DECLARE @json NVARCHAR(1000)
        SELECT @json = N'{
            "Person": [
                {
                    "BusinessEntityID": 285,
                    "FirstName": "Syed",
                    "LastName": "Abbas"
                    },
                    {
                    "BusinessEntityID": 293,
                    "FirstName": "Catherine",
                    "LastName": "Abel"
                    },
                    {
                        "BusinessEntityID": 295,
                        "FirstName": "Kim",
                        "LastName": "Abercrombie"
                    }
                    ]
                    }'
                select BusinessEntityID, FirstName, LastName
                FROM OPENJSON(@json, '$.Person')
                WITH(
                    BusinessEntityID INT,
                    FirstName varchar(500),
                    LastName varchar(500)
                    ) as Person ''')
        for row in sqljson.cursor:
            print(row)
        print()

      
obj1 = sqljson("converter")
obj1.queryjson()






from turtle import clear
import pyodbc
import os
import subprocess

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=GWTN141-10;"
    "Database=AdventureWorks2019;"
    "Trust_Connection=yes;"
)

testprog=int(input("Enter any value to test options or 0 to end::"))
while(testprog!=0):
    print("Sql and Json Queries Options \n1. Read Sql Server Data \n2. Like Query")
    print("3. IN Query \n4. Between Query \n5. Logical Operation Query")
    print("6. Join Query \n7. Convert to Json \n8. Query Json")
    option=int(input("Enter your choice of query::"))
    if(option==1):
        subprocess.call("python sqljson1read.py 1", shell=True)
    
    elif(option==2):
        subprocess.call("python sqljson2like.py", shell=True)
    
    elif(option==3):
        subprocess.call("python sqljson3INqry.py", shell=True)
    
    elif(option==4):
        subprocess.call("python sqljson4between.py", shell=True)
    elif(option==5):
        subprocess.call("python sqljson5lessthanqry.py", shell=True)
    #    os.system("exec C:\Users\compu\Desktop\sqljson4between.py")
    elif(option==6):
        subprocess.call("python sqljson6joinqry.py", shell=True)
    #    obj1.joinqry()
    elif(option==7):
        subprocess.call("python sqljson7ConverttOjson.py", shell=True)
    #    obj1.ConverttOjson()
    elif(option==8):
        subprocess.call("python sqljson8queryjson.py", shell=True)
    #    obj1.queryjson()
    testprog=int(input("\n Enter any value to test options or 0 to end::"))





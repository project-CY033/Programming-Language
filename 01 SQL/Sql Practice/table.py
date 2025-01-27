import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="College@kali90",database="Musharraf")
db_cursor=mydb.cursor()
#db_cursor.execute("create table Emp(Roll int,Name varchar(20))")    # this create table by the name of "Emp" in Musharraf database 
db_cursor.execute("show tables")

#print("Table created.....")

# to see how many tables then 
for i  in db_cursor:
    print(i)

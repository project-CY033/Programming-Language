import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="College@kali90")

db_cursor=mydb.cursor()
db_cursor.execute("create database Musharraf")
print("Databaas created ")

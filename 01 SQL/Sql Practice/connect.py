import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="College@kali90")
print(mydb,"connection established")
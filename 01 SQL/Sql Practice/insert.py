'''

import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="College@kali90",database="Musharraf")
db_cursor=mydb.cursor()

db_cursor.execute("insert into Emp(Roll,Name) values(%s,%s)",(33,"khan")) # this insert one record at a time 
mydb.commit()
print(db_cursor,"Record inserted.....")



'''


import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="College@kali90",database="Musharraf")
db_cursor=mydb.cursor()

db_insert="insert into Emp(Roll,Name) values(%s,%s)"
db_list=[(10,"Aryan"),(17,"Darshan"),(33,"Musharraf")]

db_cursor.executemany(db_insert,db_list)
mydb.commit()
print(db_cursor.rowcount, "Miltiple values inserted...")
import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="College@kali90",database="Musharraf")
db_cursor=mydb.cursor()
db_updatedata="update Musharraf.Emp set Roll=%s where Name=%s"
db_value=(1,"khan")


db_cursor.execute(db_updatedata,db_value)
mydb.commit()
print("Data updated")
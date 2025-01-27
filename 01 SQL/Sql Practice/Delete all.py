import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="College@kali90",database="Musharraf")
db_cursor=mydb.cursor()


db_delet="truncate table Musharraf.Emp"
# db_value=("khan",)
# db_cursor.execute(db_delet,db_value)
db_cursor.execute(db_delet)
mydb.commit()
print(" All record deletedd....")
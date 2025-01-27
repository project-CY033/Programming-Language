import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="College@kali90",database="Musharraf")
db_cursor=mydb.cursor()

db_cursor.execute("select * from Musharraf.Emp")
for db_data in db_cursor.fetchall():
# db_select=db_cursor.fetchall()
    print(db_data)
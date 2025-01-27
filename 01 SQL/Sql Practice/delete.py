import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="College@kali90",database="Musharraf")
db_cursor=mydb.cursor()

db_delet="delete from Musharraf.Emp where Roll=%s" # delet redord from roll no you can also delet from name now you can used "Name" at the place of "Roll"
db_value=(1,)
db_cursor.execute(db_delet,db_value)
mydb.commit()
print("record deletedd....")


# if you want to delet all record  from table use "truncate"
'''
import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="College@kali90",database="Musharraf")
db_cursor=mydb.cursor()


db_delet="truncate table Musharraf.Emp"
# db_value=("khan",)
# db_cursor.execute(db_delet,db_value)
db_cursor.execute(db_delet)
mydb.commit()
print(" All record deletedd....")

'''
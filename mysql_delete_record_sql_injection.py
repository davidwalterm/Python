import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"

addr = ("Yellow Garden 2", )

mycursor.execute(sql, addr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
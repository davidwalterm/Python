import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "pass",
    database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
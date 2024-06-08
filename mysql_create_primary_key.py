import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "pass",
    database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#If this page is executed with no error, the table "customers" now has a primary key
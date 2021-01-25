import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
    database="mydatabase"
)

mycursor = mydb.cursor()



'''Create db, table and columns'''
# mycursor.execute("CREATE DATABASE VeganCafes")
# mycursor.execute("CREATE TABLE Cafe (id INT AUTO_INCREMENT PRIMARY KEY, name CHAR(255), phone CHAR(255), tags CHAR(255), adress CHAR(255))")
# mycursor.execute("ALTER TABLE Cafe ADD location CHAR(255), ADD mailindex CHAR(255), ADD raiting CHAR(255)")
mycursor.execute("ALTER TABLE Cafe ADD latitude CHAR(255), ADD longitude CHAR(255)")

# Program to navigate through databases and tables

import mysql.connector

user = input("Username: ")
password = input("Password: ")

connection = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="")


cursor = connection.cursor()

cursor.execute("SHOW DATABASES")
result = cursor.fetchall()
for db in result:
    print(db[0])

db = input("Select a database")
cursor.execute(f"USE {db}")

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
print("Available tables:")
for tbl in tables:
    print(tbl[0])

table = input("Which table do you want to inspect? ")


cursor.execute(f"SELECT * FROM {table}")

result = cursor.fetchall()
print(f"Contents of table {table}:")
for row in result:
    print(row)

cursor.close()
connection.close()

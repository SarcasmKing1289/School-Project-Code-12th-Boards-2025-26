# Program to calculate total expenses from employee salary database

import mysql.connector

user = input("Username: ")
password = input("Password: ")

connection = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="SCHOOL_PROJECT_12A3")


cursor = connection.cursor()


cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
print("Available tables:")
for tbl in tables:
    print(tbl[0])

table = "employee_list"

cursor.execute(f"SELECT salary FROM {table}")

result = cursor.fetchall()
print(f"Contents of table {table}:")
total = 0
for row in result:
    total += row[0]

print(f"Total expenses on salaries: {total}")

cursor.close()
connection.close()

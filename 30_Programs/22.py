# ADDING DATASETS
import mysql.connector

user = input("Username: ")
password = input("Password: ")

connection = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="SCHOOL_PROJECT_12A3")

table = input("Which table do you want to append to? ")

cursor = connection.cursor()

name = input("Enter name: ")
employee_id = input("Enter employee ID: ")
salary = input("Enter salary: ")

cursor.execute(f"INSERT INTO {table} (name, emp_ID, salary) VALUES ('{name}', {employee_id}, {salary})")

cursor.execute(f"SELECT * FROM {table}")

result = cursor.fetchall()

cursor.close()
connection.close()

print("Data appended successfully. Current contents of the table:")
for row in result:
    for data in row:
        print(data, end=" ")
    print()
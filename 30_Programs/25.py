# Program to sort employees based on their salaries
import mysql.connector

user = input("Username: ")
password = input("Password: ")

connection = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="SCHOOL_PROJECT_12A3")

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee_list")

result = cursor.fetchall()

reverse = input("Do you want to sort in descending order? (yes/no): ").strip().lower()

if reverse == "yes" or reverse == "y":
    result.sort(key=lambda x: x[2], reverse=True)
else:
    result.sort(key=lambda x: x[2]) 

i = 1
for row in result:
    print(i, end=". ")
    for data in row:
        print
        print(data, end=" ")
    print()

    i += 1


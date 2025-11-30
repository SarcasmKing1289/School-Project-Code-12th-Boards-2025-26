# DISPLAYING CURRENT DATA IN TABLE FROM DATABASE
import mysql.connector

user = input("Username: ")
password = input("Password: ")

connection = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="SCHOOL_PROJECT_12A3")


table = input("Which table do you want to inspect? ")

cursor = connection.cursor()

cursor.execute(f"SELECT * FROM {table}")

result = cursor.fetchall()

cursor.close()
connection.close()

n=1
for row in result:
    print(n, end=". ")
    for data in row:
        print(data, end=" ")
    print()
    n+=1
import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

# name = input("Enter your Name: ")
# email = input("Enter your email: ")
# age = int(input("Enter your age : "))

# cursor.execute("INSERT INTO users(name, email, age) VALUES(?,?,?)",(name, email, age))



cursor.execute("INSERT INTO users(name, email, age) VALUES(?,?,?)",("Sankalp", "Sankalp@gmail.com", 19))

cursor.execute("INSERT INTO users(name, email, age) VALUES(?,?,?)",("Rahul", "Rahul@gmail.com", 18))

cursor.execute("INSERT INTO users(name, email, age) VALUES(?,?,?)",("Ravi", "Ravi@gmail.com", 20))

cursor.execute("INSERT INTO users(name, email, age) VALUES(?,?,?)",("Arpit", "Arpit@gmail.com", 21))

conn.commit()
conn.close()

print("Users Created !!!")
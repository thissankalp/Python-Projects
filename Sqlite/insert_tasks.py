import sqlite3

conn = sqlite3.connect("tasks.db")

cursor = conn.cursor()

task = input("Enter your task : ")

cursor.execute("INSERT INTO tasks(task) VALUES(?)", (task,))
conn.commit()
conn.close()
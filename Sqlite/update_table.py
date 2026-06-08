import sqlite3

conn = sqlite3.connect("tasks.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM tasks")

rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]} | Task: {row[1]}")

try:
    index = int(input("Enter ID for the task you want to update : "))
except ValueError:
    print("Enter a valid number !!")
    conn.close()
    exit()

task = input("Enter updated task : ")

cursor.execute("UPDATE tasks SET task=? WHERE id=?", (task, index, ))

if cursor.rowcount == 0:
    print("Task ID not found!")
else:
    print(f"Task {index} updated!")

conn.commit()
conn.close()
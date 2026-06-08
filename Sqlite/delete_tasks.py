import sqlite3

conn = sqlite3.connect("tasks.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM tasks")

rows = cursor.fetchall()
print(rows)

try:
    index = int(input("Enter ID for the task you want to delete : "))
except ValueError:
    print("Enter a valid number !!")
    conn.close()
    exit()

cursor.execute("DELETE FROM tasks WHERE id=?", (index, ))

conn.commit()
conn.close()
import sqlite3

conn = sqlite3.connect("tasks.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM tasks")

rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]} | Task: {row[1]}")

conn.close()
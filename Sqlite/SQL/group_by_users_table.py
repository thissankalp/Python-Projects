import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute("SELECT age, COUNT(*) FROM users GROUP BY age")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
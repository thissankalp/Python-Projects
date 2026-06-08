import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM users")

count = cursor.fetchone()

print(count[0])

conn.close()
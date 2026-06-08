import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

print()
print("Users with age greater than 18 years:")
cursor.execute("SELECT * FROM users WHERE age > ?", (18,))
rows = cursor.fetchall()
for row in rows:
    print(row)

print()
print("Users with age greater than 20 years:")
cursor.execute("SELECT * FROM users WHERE age > ?", (20,))
rows = cursor.fetchall()
for row in rows:
    print(row)

print()
print("Users with age lesser than 20 years:")
cursor.execute("SELECT * FROM users WHERE age < ?", (20,))
rows = cursor.fetchall()
for row in rows:
    print(row)

print()
print("Users with name Sankalp:")
cursor.execute("SELECT * FROM users WHERE name = ?", ("Sankalp",))
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
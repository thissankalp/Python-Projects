import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

print()
print("Users sorted by age in ascending order : ")
cursor.execute("SELECT * FROM users ORDER BY age ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)

print()
print("Users sorted by age in descending order : ")
cursor.execute("SELECT * FROM users ORDER BY age DESC")
rows = cursor.fetchall()
for row in rows:
    print(row)

print()
print("Users sorted by name in ascending order : ")
cursor.execute("SELECT * FROM users ORDER BY name ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()

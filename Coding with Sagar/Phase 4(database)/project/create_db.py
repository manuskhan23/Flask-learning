import sqlite3

conn = sqlite3.connect("site.db")

cursor = conn.cursor()  # also fixed spelling because "corsur" hurt my soul

cursor.execute("""
CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

conn.commit()
conn.close()
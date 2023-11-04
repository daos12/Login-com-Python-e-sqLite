import sqlite3

conn = sqlite3.connect('UserData.db')

cursor = conn.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS Users(
       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       email TEXT NOT NULL,
       user TEXT NOT NULL,
       password TEXT NOT NULL
   );
""")

print("Conectado ao Banco de dados")
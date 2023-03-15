import sqlite3

#  ======= creating connection and cursor ======
connection = sqlite3.connect('DB.sqlite')
cursor = connection.cursor()
# working with database

query  = ('CREATE TABLE IF NOT EXISTS users2 ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'first_name TEXT,'
         'last_name TEXT,'
         'age INTEGER,'
         'UNIQUE(first_name, last_name))')
cursor.execute(query)
connection.commit()
query_1 = ("INSERT INTO users (first_name, last_name, age) VALUES('Valerii','Ivanov', 23)")
cursor.execute(query_1)
connection.commit()
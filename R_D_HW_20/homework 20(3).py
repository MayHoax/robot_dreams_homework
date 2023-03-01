import sqlite3

#  ======= creating connection and cursor ======
connection = sqlite3.connect('DB.sqlite')
cursor = connection.cursor()
# working with database

query = ('CREATE TABLE IF NOT EXISTS users1('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'first_name TEXT NOT NULL,'
         'last_name TEXT NOT NULL,'
         'age INTEGER)')

connection.commit()
query_1 = ("INSERT INTO users (first_name, last_name, age) VALUES('','', 23)")
cursor.execute(query_1)
connection.commit()
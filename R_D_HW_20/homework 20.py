import sqlite3

#  ======= creating connection and cursor ======
connection = sqlite3.connect('DB.sqlite')
cursor = connection.cursor()
# working with database

query = ('CREATE TABLE IF NOT EXISTS users ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'first_name TEXT,'
         'last_name TEXT,'
         'age INTEGER)')

cursor.execute(query)
connection.commit()

query_1 = ("INSERT INTO users (first_name, last_name, age) VALUES('Valerii','Ivanov', 23)")
query_2 = ("INSERT INTO users (first_name, last_name, age) VALUES('George', 'Lavrod', 26)")
query_3 = ("INSERT INTO users (first_name, last_name, age) VALUES('Ilya', 'Ulichev', 24)")
query_4 = ("INSERT INTO users (first_name, last_name, age) VALUES('Oleksii', 'Klymenok', 23)")
query_5 = ("INSERT INTO users (first_name, last_name, age) VALUES('Deidara', 'Mazukaga', 228)")

cursor.execute(query_1)
cursor.execute(query_2)
cursor.execute(query_3)
cursor.execute(query_4)
cursor.execute(query_5)


connection.commit()





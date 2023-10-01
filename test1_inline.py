import sqlite3


connection = sqlite3.connect("anketa.db")
cursor = connection.cursor()
a = cursor.execute('SELECT*FROM anketa WHERE user_id = 297003991').fetchall()
for i in a:

    print(i)
connection.commit()


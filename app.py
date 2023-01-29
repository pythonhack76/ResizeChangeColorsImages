import sqlite3

connect = sqlite3.connect('data.db')


connect.execute("DROP TABLE IF EXISTS USER")
connect.execute('''CREATE TABLE USER
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL);''')

connect.close() 
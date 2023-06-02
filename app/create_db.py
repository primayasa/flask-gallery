import sqlite3 as sql

#connect to SQLite
con = sql.connect('gallery.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users")

#Create users table  in db_web database
sql =('''CREATE TABLE IF NOT EXISTS images
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_name TEXT,
                image_path TEXT)''')
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()
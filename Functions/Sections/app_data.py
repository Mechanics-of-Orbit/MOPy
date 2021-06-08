import sqlite3
conn= sqlite3.connect('appdatabase.db')
c= conn.cursor()

c.execute("SELECT * FROM planetary_factsheet_metric")

c.execute(" SELECT * FROM planetary_ephemeredis")
print(c.fetchall())

conn.commit()
conn.close()
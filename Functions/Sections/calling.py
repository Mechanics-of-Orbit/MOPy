import sqlite3

conn = sqlite3.connect('appdatabase.db')

c = conn.cursor()
c.execute("SELECT * FROM planetary_ephemeredis")
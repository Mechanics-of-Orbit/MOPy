import sqlite3 
conn = sqlite3.connect('info.db')
c = conn.cursor()


c.execute("SELECT * FROM planetary_fact_sheet_metric")

print(c.fetchone())  

  

conn.commit()

conn.close()
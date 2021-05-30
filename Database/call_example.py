import sqlite3
import sys
from os import path


db = sqlite3.connect("info.db")
cursor = db.cursor()

major_body = "Earth"
mass = cursor.execute(''' Select ''')

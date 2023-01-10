import sqlite3

db = sqlite3.connect('MajorBody_data.db')
major_body = "Earth"
cursor = db.cursor()
Data = cursor.execute('''SELECT * from Planet_Table WHERE Major_body==?''',[major_body])

for row_number, row_data in enumerate(Data):
    major_body_data = row_data[2]
return [major_body_data]

import sqlite3

d = sqlite3.connect(r'DB/MajorBody_data.db')
cursor = d.cursor()
r = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[MiB])
for row_num, row_dat in enumerate(r):
    MiB_mass = row_dat[1]
    MiB_radius = row_dat[2] / 2
    r_maj_to_min = row_dat[8]

print(MiB_mass)
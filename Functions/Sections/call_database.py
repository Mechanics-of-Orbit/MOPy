import sqlite3
import math

db = sqlite3.connect("Functions/Sections/DB/MajorBody_data.db")
cursor = db.cursor()
        
class call():
    def mass(Major_Body):
        major_body = str(Major_Body)
        major_body = major_body.strip()
        result = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[major_body])
        for row_number, row_data in enumerate(result):
            major_body_mass = row_data[1]
        return major_body_mass
    
    def radius(Major_Body):
        major_body = str(Major_Body)
        major_body = major_body.strip()
        result = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[major_body])
        for row_number, row_data in enumerate(result):
            major_body_radius = row_data[2]/2
        return major_body_radius

    def dist_frm_sun(Major_Body):
        major_body = str(Major_Body)
        major_body = major_body.strip()
        result = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[major_body])
        for row_number, row_data in enumerate(result):
            dist_frm_sun = row_data[8]
        return dist_frm_sun

def raund(f, n):
    rSOI = str(f).split('e')
    rSOI1 = str(round(float(rSOI[0]),n))
    rSOI = rSOI1 + 'e' + str(rSOI[1])
    return rSOI
    
if __name__ == '__main__':
    Major_Body = 'Earth'
    major_body_mass = call.mass(Major_Body)
    print(major_body_mass)
    major_body_radius = call.radius(Major_Body)
    print(major_body_radius)
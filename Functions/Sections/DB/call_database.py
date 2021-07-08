import sqlite3
import math


db = sqlite3.connect("Functions/Sections/DB/MajorBody_data.db")
cursor = db.cursor()

class call():
    def data(Major_Body, data_type):

        title = {'mass':1, 'maj_bdy_rad':2, 'density':3, 'acc_due_to_grty':4, 'esc_vel':5, 'rot_perd':6, 'len_of_day':7, 'dist_frm_sun':8, 'perihelion':9, 'apohelion':10, 'orital_period':11, 'orbital_velocity':12, 'orbital_inclination':13, 'orital_eccentricity':14, 'obliquity_to_orbit':15, 'mean_temperature':16, 'number_of_moons':17, 'ring_system':18, 'global_magnetic_field':19}
        key = title[data_type]
        
        major_body = str(Major_Body)
        major_body = major_body.strip()
        result = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[major_body])
        for row_number, row_data in enumerate(result):
            major_body_data = row_data[key]
        return [major_body_data,major_body]

def raund(f, n):
    rSOI = str(f).split('e')
    rSOI1 = str(round(float(rSOI[0]),n))
    rSOI = rSOI1 + 'e' + str(rSOI[1])
    return rSOI
    

 
    
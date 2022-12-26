import sqlite3

db = sqlite3.connect("Functions/Sections/DB/MajorBody_data.db")
cursor = db.cursor()

class call():
    def data(Major_Body, data_type):

        title = {'mass':1, 'diameter':2,'density':3, 'acc_due_to_grty':4, 'esc_vel':5, 'rot_perd':6, 'len_of_day':7, 'dist_frm_sun':8, 'perihelion':9, 'apohelion':10, 'orital_period':11, 'orbital_velocity':12, 'orbital_inclination':13, 'orital_eccentricity':14, 'obliquity_to_orbit':15, 'mean_temperature':16, 'number_of_moons':17, 'ring_system':18, 'global_magnetic_field':19, 'radius':20}

        key = title[data_type]
        print(key)
        major_body = str(Major_Body)
        major_body = major_body.strip()
        print(major_body)
        i = cursor.execute('''SELECT * from Planet_Table WHERE Major_Body==?''',[major_body])
        print(i)
        

        return [major_body]

if __name__ == '__main__':
    call.data("Earth","radius")
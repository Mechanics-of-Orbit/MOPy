import sqlite3

conn = sqlite3.connect("Functions\Sections\DB\DataTables\MajorBody_data.db")
cursor = conn.cursor()

def planet_data(major_body,major_body_data):
    major_body = str(major_body).strip()
    major_body_data = str(major_body_data).strip()
    if major_body == "Select the Major Body":
        print("Scroll down and select the major body from the list")
    cursor.execute("SELECT * FROM Planet_Table")
    Celestial_Bodies = {"Mercury":0, "Venus":1, "Earth":2, "Moon":3, "Mars":4, "Jupiter":5, "Saturn":6, "Uranus":7, "Neptune":8, "Pluto":9, "Sun":10}  
    Celestial_Bodies_features = {"Mass":1, "Diameter":2, "Density":3, "Acceleration_due_to_Gravity":4, "Escape_Velocity":5, "Rotation_Period":6, "Length_of_Day":7, "Distance_from_sun":8, "Radius":20}   
    Major_Body = Celestial_Bodies[major_body]
    Major_Body_Data = Celestial_Bodies_features[major_body_data]
    out_data = cursor.fetchall()[Major_Body][Major_Body_Data]
    return[out_data,major_body]

def planetary_ephemeris(major_body, major_body_data):
    major_body = str(major_body).strip()
    major_body_data = str(major_body_data).strip()
    cursor.execute('SELECT * FROM PlanetaryEphemeris')
    Celestial_Bodies = {"Mercury":0, "Venus":1, "Earth":2, "Mars":3, "Jupiter":4, "Saturn":5, "Uranus":6, "Neptune":7, "Pluto":8, "Sun":10}
    Celestial_Bodies_features = {'aAU':1,'aAU_DotaDotAUCentury-1':2,'e':3,'eDotCentury-1':4,'iDeg':5,'iDotDegCentury-1':6,'RAANDeg':7,'RAANDotDegCentury-1':8,'OmegaDeg':9,'omegaDotDegCentury-1':10,'nuDeg':11,'nuDotDegCentury-1':12}
    Major_Body = Celestial_Bodies[major_body]
    Major_Body_Data = Celestial_Bodies_features[major_body_data]
    out_data = cursor.fetchall()[Major_Body][Major_Body_Data]
    return[out_data, major_body]


def raund(f, n):
    num = f
    num = str(num)
    num = num.split('.')
    num_0 = num[0]
    num_0_len = len(num_0)
    num_1 = num[1]
    if num_0_len > 3:
        num = round(f, n)
        if num_0[3] == '0' and num_0[4] == '0':
            num = num_0[0:3] + 'e' + '+' + str(num_0_len - 3)
        elif num_0[3] == '0' and num_0[4] != '0':
            num = num_0[0:3] + '.' + num_0[3:5] + 'e' + '+' + str(num_0_len - 3)
        elif num_0[3] != '0' and num_0[4] == '0':
            num = num_0[0:3] + '.' + num_0[3] + 'e' + '+' + str(num_0_len - 3)
        else:
            num = num_0[0:3] + '.' + num_0[3:5] + 'e' + '+' + str(num_0_len - 3)
    elif num_0_len == 1:
        if num_1[0] == '0' and num_1[1] == '0' and num_1[2] == '0':
            num = num_1[2] + '.' + num_1[3] + num_1[4]
        elif num_1[0] == '0' and num_1[1] != '0' and num_1[2] == '0':
            num = num_1[1] + num_1[2] + '.' + num_1[3] + num_1[4]
        elif num_1[0] == '0' and num_1[1] == '0' and num_1[2] != '0':
            num = num_1[2] + '.' + num_1[3] + num_1[4]
        elif num_1[0] != '0' and num_1[1] == '0' and num_1[2] == '0':
            num = num_1[0] + num_1[1] + num_1[2] + '.' + num_1[3] + num_1[4]
        elif num_1[0] != '0' and num_1[1] != '0' and num_1[2] == '0':
            num = num_1[0] + num_1[1] + num_1[2] + '.' + num_1[3] + num_1[4]
        elif num_1[0] != '0' and num_1[1] == '0' and num_1[2] != '0':
            num = num_1[0] + num_1[1] + num_1[2] + '.' + num_1[3] + num_1[4]
        elif num_1[0] != '0' and num_1[1] != '0' and num_1[2] != '0':
            num = num_1[0] + num_1[1] + num_1[2] + '.' + num_1[3] + num_1[4]
    else:
        num = round(f, n)
        num = str(num)
        num = num[0] +'.' + num[1]
    return num



    



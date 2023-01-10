import sqlite3

conn = sqlite3.connect("modules\DB\DataTables\MajorBody_data.db")
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

def raund(f, n):
    rSOI = str(f).split('e')
    rSOI1 = str(round(float(rSOI[0]),n))
    rSOI = rSOI1 + 'e' + str(rSOI[1])
    return rSOI



    



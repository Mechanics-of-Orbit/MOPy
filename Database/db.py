import sqlite3 





def show_all(): 
     # connect to database
    conn = sqlite3.connect('info.db')

    # create a cursor
    c = conn.cursor()  

    # query the database
    c.execute("SELECT rowid, * FROM planetary_fact_sheet_metric")

    items = c.fetchall()
 
    print("BODY NAME" + "\t\tMASS" + "\t\tRADIUS" + "\t\tDENSITY" + "\t\tGRAVITY" + "\t\tESCAPE VELOCITY" + "\t\tROTATION PERIOD" + "\t\tLENGTH OF DAY" + "\t\tDISTANCE FROM SUN" + "\t\tPERIHELION" + "\t\tAPEHELION" + "\t\tORBITAL PERIOD" + "\t\tORBITAL VELOCITY" + "\t\tORBITAL INCLINATION" + "\t\tORBITAL ECCENTRICITY" + "\t\tOBLIQUITY TO ORBIT" +"\t\tMEAN TEMPERATURE" + "\t\tNUMBER OF MOONS")

    for value in items:
        print( value[1] + "\t\t" + str(value[2]) + "\t\t" + str(value[3]) + "\t\t" + str(value[4]) + "\t\t" + str(value[5]) + "\t\t" + str(value[6]) + "\t\t" + str(value[7]) + "\t\t" + str(value[8]) + "\t\t" + str(value[9]) + "\t\t" + str(value[10]) + "\t\t" + str(value[11]) + "\t\t" + str(value[12]) + "\t\t" + str(value[13]) + "\t\t" + str(value[14]) + "\t\t" + str(value[15]) + "\t\t" + str(value[16]) + "\t\t" + str(value[17])     )        

    # commiot our command
    conn.commit()
   
    # close our command 
    conn.close()



from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sqlite3


def plot(r):
  
    #plotting 3-D
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(111, projection = '3d')

    r_plot = minor_body_radius

    _u,_v = np.mgrid[0:2*np.pi:20j,0:np.pi:10j]
    _x = r_plot*np.cos(_u)*np.sin(_v)
    _y = r_plot*np.sin(_u)*np.sin(_v)
    _z = r_plot*np.cos(_v)
    ax.plot_surface(_x,_y,_z, cmap = 'Blues')

    r_SoI = r

    _u_S,_v_S = np.mgrid[0:2*np.pi:20j,0:np.pi:10j]
    _x_S = r_SoI*np.cos(_u_S)*np.sin(_v_S)
    _y_S = r_SoI*np.sin(_u_S)*np.sin(_v_S)
    _z_S = r_SoI*np.cos(_v_S)
    ax.plot_wireframe(_x_S,_y_S,_z_S, color = 'r')
    
    plt.show()


def SoI(MiB, MaB):
    d = sqlite3.connect(r"DB/MajorBody_data.db")
    cursor = d.cursor()
    r = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[MiB])
    for row_num, row_dat in enumerate(r):
        MiB_mass = row_dat[1]
        MiB_radius = row_dat[2] / 2
        r_maj_to_min = row_dat[8]
    
    #r1 = cursor.execute(''' SELECT * from Planet_Table WHERE Major_body==?''',[MaB])
    #for row_num2, row_dat2 in enumerate(r1):
        #MaB_mass = row_dat2[1]
        
    #MiB_mass = 5.972e24
    MaB_mass = 1.989e30
    #r_maj_to_min = 149597870
    #MiB_radius = 6378
    rSOI = (r_maj_to_min*(MiB_mass/MaB_mass)**(2/5))
    return [rSOI, rSOI/MiB_radius]

#if __name__ == '__main__':
    #MaB1 = "Sun"
    #MiB1 = "Earth"    
    #[rSOI, rSOIMiB] = SoI(MiB1,MaB1)
    #print([rSOI, rSOIMiB])
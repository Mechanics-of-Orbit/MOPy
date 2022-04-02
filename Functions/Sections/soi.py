from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Functions.Sections.DB.call_database import *



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



def SOICalc(MinorBody):
    [MiB_mass, a] = planet_data(MinorBody, 'mass')
    [MiB_radius,a] = planet_data(MinorBody, 'radius')
    [MaB_mass, a] = planet_data("Sun", 'mass')
    [r_maj_to_min, a] = planet_data(MinorBody, 'dist_frm_sun')
    # print(MiB_mass, MiB_radius, MaB_mass, r_maj_to_min)
    rSOI = (r_maj_to_min*(MiB_mass/MaB_mass)**(2/5))
    return [rSOI, rSOI/MiB_radius]

if __name__ == '__main__':  
    [rSOI, rSOIMiB] = SOICalc("Earth")
    print([rSOI, rSOIMiB])
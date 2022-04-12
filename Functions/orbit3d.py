import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.patches import Ellipse
import Sections.VPCO as VPCO

class OrbitPlot():
    def plotOrbitMPL(mu, rMB, ra, rp, mMB, thetadi, thetadf):      
        theta = np.linspace(thetadi, thetadf, 500)
        # fig, ax = plt.subplots()
        val = VPCO.CalculateCircularElliptical.perapo(rp, ra, mMB)
        ri=(val[4]**2/mu)/(1+val[0]*np.cos(theta))
        x1 = ri*np.sin(theta)
        y1 = ri*np.cos(theta)
        return x1, y1
    
    def hohmannTransfer(ra1,rp1, ra2, rp2, mu, rMB, mMB):
        Orbit1 = OrbitPlot.plotOrbitMPL(mu, rMB, ra1, rp1, mMB, np.pi, 3*np.pi)
        TransferOrbit1 = OrbitPlot.plotOrbitMPL(mu, rMB, ra2, rp1, mMB, np.pi/2, np.pi*3/2)
        Orbit2 = OrbitPlot.plotOrbitMPL(mu, rMB, ra2, rp2, mMB, 2*np.pi, 0)
        plt.plot(Orbit1[0], Orbit1[1])
        plt.plot(TransferOrbit1[0], TransferOrbit1[1])
        plt.plot(Orbit2[0], Orbit2[1])
        plt.show()
        # return [Orbit1, TransferOrbit1, Orbit2]
    
    def biellipticalHohmannTransfer():
        pass
        
 

if __name__ == "__main__":
    # a = OrbitPlot.plotOrbitMPL(3.986e5, 6378, 8000, 7000, 5.9722e24, 2*np.pi)
    # b = OrbitPlot.plotOrbitMPL(3.986e5, 6378, 10000, 8000, 5.9722e24, 2*np.pi)
    a = OrbitPlot.hohmannTransfer(8000, 7000, 10000, 9000, 3.986e5, 6378, 5.9722e24)
    # b = VPCO.CalculateCircularElliptical.semiecc(7500, 0.1, 5.9722e24)
    # print(b)
    # rMB = 6378
    # sma = 25000
    # ra = 37500
    # rp = 12500
    # mMB = 5.9722e24
    # a = OrbitPlot.plotOrbitMPL(3.986e5, rMB, ra, rp, mMB, 0, 2*np.pi)
    # # img = plt.imread("Functions/Assets/Models/hi_res_tex/stars.jpg")
    # # fig, ax = plt.subplots()
    # # plt.imshow(img)
    # # plt.plot(a[0],a[1])
    # theta = np.linspace(0, 2*np.pi, 500)
    # rx = 6378*np.sin(theta)
    # ry = 6378*np.cos(theta)
    
    # # plt.axes('equal')
    # ax = plt.axes()
    # ax.set_facecolor("black")
    # ax.plot(rx, ry, color="white", linewidth=3)
    # ax.axes('equal\')
    # plt.show()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.patches import Ellipse
import Functions.Sections.VPCO as VPCO
from matplotlib import style

import sys
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class OrbitPlot():
    def plotOrbitMPL(mu, ra, rp, thetadi, thetadf):      
        theta = np.linspace(thetadi, thetadf, 1000)
        e = (ra-rp)/(ra + rp)
        h = (rp*(1+e)*mu)**0.5
        ri=(h**2/mu)/(1+e*np.cos(theta))
        x1 = ri*np.sin(theta)
        y1 = ri*np.cos(theta)
        return x1, y1, ri
    
    def hohmannTransfer(ra1,rp1, ra2, rp2, mu, rMB):
        Orbit1 = OrbitPlot.plotOrbitMPL(mu, ra1, rp1, 0, 2*np.pi)
        TransferOrbit1 = OrbitPlot.plotOrbitMPL(mu, ra2, rp1, 0, np.pi)
        Orbit2 = OrbitPlot.plotOrbitMPL(mu,ra2, rp2, 0, 2*np.pi)
        MajorBodyPlot = OrbitPlot.plotOrbitMPL(mu,rMB, rMB, 0, 2*np.pi)
        # style.use("dark_background")
        # plt.plot(Orbit1[0], Orbit1[1], "r")
        # plt.plot(TransferOrbit1[0], TransferOrbit1[1], "yellow", LineStyle = "dotted")
        # plt.plot(Orbit2[0], Orbit2[1],"green")
        # plt.fill(MajorBodyPlot[0], MajorBodyPlot[1], "b")
        # plt.axis('equal')
        # plt.title("Hohmann Transfer")
        # plt.show()
        return [Orbit1, TransferOrbit1, Orbit2]
    
    def biellipticalHohmannTransfer(mu, rMB, ra1,rp1, ra2, rp2, rt1a = None, rt1p = None):
        Orbit1 = OrbitPlot.plotOrbitMPL(mu, ra1, rp1, 0, 2*np.pi)
        if rt1a != None:
            TransferOrbit1 = OrbitPlot.plotOrbitMPL(mu, rt1a, rp1, 0, np.pi)
            TransferOrbit2 = OrbitPlot.plotOrbitMPL(mu, rt1a, rp2, np.pi, 2*np.pi)
        elif rt1p != None:
            TransferOrbit1 = OrbitPlot.plotOrbitMPL(mu, ra1, rt1p, 0, np.pi)
            TransferOrbit2 = OrbitPlot.plotOrbitMPL(mu, rt1p, rp2, np.pi, 2*np.pi)
        Orbit2 = OrbitPlot.plotOrbitMPL(mu,ra2, rp2, 0, 2*np.pi)
        MajorBodyPlot = OrbitPlot.plotOrbitMPL(mu,rMB, rMB, 0, 2*np.pi)
        # style.use("dark_background")
        # plt.plot(Orbit1[0], Orbit1[1], "r")
        # plt.plot(TransferOrbit1[0], TransferOrbit1[1], "yellow", LineStyle = "dotted")
        # plt.plot(TransferOrbit2[0], TransferOrbit2[1], "violet", LineStyle = "dotted")
        # plt.plot(Orbit2[0], Orbit2[1],"green")
        # plt.fill(MajorBodyPlot[0], MajorBodyPlot[1], "b")
        # plt.axis('equal')
        # plt.title("Bi-Elliptical Hohmann Transfer")
        # plt.show()
        return [Orbit1, Orbit2, TransferOrbit1, TransferOrbit2]
    
    def phasingManeuver(mu, rMB, ra1, rp1, thetaA, thetaB):
        Orbit1 = OrbitPlot.plotOrbitMPL(mu, ra1, rp1, 0, 2*np.pi)
        a1 = (ra1+rp1)/2
        e1 = (ra1-rp1)/(ra1+rp1)
        T1 = 2*np.pi*a1**(3/2)/np.sqrt(mu)
        EB = 2*np.arctan(np.sqrt((1-e1)/(1+e1))*np.tan(thetaB/2))
        tAB = T1*(EB-e1*np.sin(EB))/(2*np.pi)
        T2 = T1-tAB
        a2 = ((np.sqrt(mu)*T2)/(2*np.pi))**(2/3)
        ra2 = 2*a2-rp1
        Orbit2 = OrbitPlot.plotOrbitMPL(mu, ra2, rp1, 0, 2*np.pi)
        MajorBodyPlot = OrbitPlot.plotOrbitMPL(mu,rMB, rMB, 0, 2*np.pi)
        # style.use("dark_background")
        # plt.plot(Orbit1[0], Orbit1[1], "r")
        # plt.text(0, Orbit1[2]*np.cos(thetaA),"* Satellite-A")
        # plt.plot(Orbit2[0], Orbit2[1],"green", LineStyle = "dotted")
        # plt.text(Orbit1[2]*np.sin(thetaB), 0,"* Satellite-B")
        # plt.fill(MajorBodyPlot[0], MajorBodyPlot[1], "b")
        # plt.axis('equal')
        # plt.title("Hohmann Transfer")
        # plt.show()
        return [Orbit1, Orbit2]
        
 

if __name__ == "__main__":
    # a = OrbitPlot.plotOrbitMPL(3.986e5, 12000, 8000, 0, 2*np.pi)
    # plt.plot(a[0],a[1])
    # plt.show()
    a = OrbitPlot.hohmannTransfer(7178, 6878, 22378, 22378, 3.986e5, 6378)
    # a = OrbitPlot.biellipticalHohmannTransfer(3.986e5, 6378, 7000, 7000, 105000, 105000, rt1a = 210000)
    # a = OrbitPlot.phasingManeuver(3.986e5, 6378, 13600, 6800, 0, np.pi/2)
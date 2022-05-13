import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.patches import Ellipse
import Sections.VPCO as VPCO
from matplotlib import style

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
        TransferOrbitA = OrbitPlot.plotOrbitMPL(mu, ra2, rp1, 0, np.pi)
        Orbit2 = OrbitPlot.plotOrbitMPL(mu,ra2, rp2, 0, 2*np.pi)
        MajorBodyPlot = OrbitPlot.plotOrbitMPL(mu,rMB, rMB, 0, 2*np.pi)
        h1 = np.sqrt(2*mu)*np.sqrt(ra1*rp1/(ra1+rp1))
        htA = np.sqrt(2*mu)*np.sqrt(ra2*rp1/(ra2+rp1))
        h2 = np.sqrt(2*mu)*np.sqrt(ra2*rp2/(ra2+rp2))
        a1, aT1, a2 = (ra1+rp1)/2, (ra2+rp1)/2, (ra2+rp2)/2
        vp1, va1, vatA, vptA, vp2, va2 = h1/rp1, h1/ra1, htA/ra2, htA/rp1, h2/rp2, h2/ra2
        Tt1 = 2*np.pi*aT1^(3/2)/np.sqrt(mu)
        deltaV1 = vptA-vp1
        deltaV2 = va2-vatA
        DeltaVA = deltaV1+deltaV2
        style.use("dark_background")
        plt.plot(Orbit1[0], Orbit1[1], "r")
        plt.plot(TransferOrbitA[0], TransferOrbitA[1], "yellow", LineStyle = "dotted")
        plt.plot(Orbit2[0], Orbit2[1],"green")
        plt.fill(MajorBodyPlot[0], MajorBodyPlot[1], "b")
        plt.axis('equal')
        plt.title("Hohmann Transfer")
        plt.show()
        return deltaV1, deltaV2, DeltaVA, Tt1/2 #[Orbit1, TransferOrbitA, Orbit2]
    
    def biellipticalHohmannTransfer(mu, rMB, ra1,rp1, ra2, rp2, rt1a):
        Orbit1 = OrbitPlot.plotOrbitMPL(mu, ra1, rp1, 0, 2*np.pi)
        TransferOrbit1 = OrbitPlot.plotOrbitMPL(mu, rt1a, rp1, 0, np.pi)
        TransferOrbit2 = OrbitPlot.plotOrbitMPL(mu, rt1a, rp2, np.pi, 2*np.pi)
        Orbit2 = OrbitPlot.plotOrbitMPL(mu,ra2, rp2, 0, 2*np.pi)
        MajorBodyPlot = OrbitPlot.plotOrbitMPL(mu,rMB, rMB, 0, 2*np.pi)
        h1 = np.sqrt(2*mu)*np.sqrt(ra1*rp1/(ra1+rp1))
        ht1A = np.sqrt(2*mu)*np.sqrt(rt1a*rp1/(rt1a+rp1))
        ht2A = np.sqrt(2*mu)*np.sqrt(rt1a*rp2/(rt1a+rp2))
        h2 = np.sqrt(2*mu)*np.sqrt(ra2*rp2/(ra2+rp2))
        a1, aT1A, aT2A, a2 = (ra1+rp1)/2, (rt1a+rp1)/2, (rt1a+rp2)/2, (ra2+rp2)/2
        vp1, va1, vat1A, vpt1A, vat2A, vpt2A ,vp2, va2 = h1/rp1, h1/ra1, ht1A/ra2, ht1A/rp1, ht2A/rt1a, ht2A/rp2 ,h2/rp2, h2/ra2
        deltaV1 = vpt1A-vp1
        deltaVtA = vat1A-vat2A
        deltaV2 = vp2-vpt2A
        DeltaVA = deltaV1+deltaV2+deltaVtA
        TtA = 0.5(((2*np.pi)*(aT1A)^(3/2))/(np.sqrt(mu)) + ((2*np.pi)*(aT2A)^(3/2))/(np.sqrt(mu)))
        style.use("dark_background")
        plt.plot(Orbit1[0], Orbit1[1], "r")
        plt.plot(TransferOrbit1[0], TransferOrbit1[1], "yellow", LineStyle = "dotted")
        plt.plot(TransferOrbit2[0], TransferOrbit2[1], "violet", LineStyle = "dotted")
        plt.plot(Orbit2[0], Orbit2[1],"green")
        plt.fill(MajorBodyPlot[0], MajorBodyPlot[1], "b")
        plt.axis('equal')
        plt.title("Bi-Elliptical Hohmann Transfer")
        plt.show()
        return deltaV1, deltaVtA, deltaV2, DeltaVA, TtA
    
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
        style.use("dark_background")
        plt.plot(Orbit1[0], Orbit1[1], "r")
        plt.text(0, Orbit1[2]*np.cos(thetaA),"* Satellite-A")
        plt.plot(Orbit2[0], Orbit2[1],"green", LineStyle = "dotted")
        plt.text(Orbit1[2]*np.sin(thetaB), 0,"* Satellite-B")
        plt.fill(MajorBodyPlot[0], MajorBodyPlot[1], "b")
        plt.axis('equal')
        plt.title("Hohmann Transfer")
        plt.show()
        return T1, tAB, T2
        
 

if __name__ == "__main__":
    # a = OrbitPlot.plotOrbitMPL(3.986e5, 6378, 8000, 7000, 5.9722e24, 2*np.pi)
    # b = OrbitPlot.plotOrbitMPL(3.986e5, 6378, 10000, 8000, 5.9722e24, 2*np.pi)
    # a = OrbitPlot.hohmannTransfer(7178, 6878, 22378, 22378, 3.986e5, 6378)
    # a = OrbitPlot.biellipticalHohmannTransfer(3.986e5, 6378, 7000, 7000, 105000, 105000, rt1a = 210000)
    a = OrbitPlot.phasingManeuver(3.986e5, 6378, 13600, 6800, 0, np.pi/2)
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
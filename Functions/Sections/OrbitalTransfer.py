from numpy import *
import matplotlib.pyplot as plt
from matplotlib import style

def initial_Values(ra1, rp1, ra2, rp2, rat2):
    rat = rat2
    rpt = rp1
    e1 = (ra1 - rp1)/(ra1 + rp1)
    e2 = (ra2 - rp2)/(ra2 + rp2)
    mu = 3.986e5
    ai=(ra1+rp1)/2
    af=(ra2+rp2)/2
    at=(rp1+ra2)/2
    deltav1=sqrt((2*mu/rpt)-(mu/at))-sqrt((2*mu/rp1)-(mu/ai))
    deltav2=sqrt((2*mu/ra2)-(mu/af))-sqrt((2*mu/ra2)-(mu/at))
    deltavt=deltav1+deltav2
    Tt=sqrt(((4*pi**2)/mu)*at**3)/2
    et1=(rat2-rp1)/(rat2+rp1)
    et2=(rat2-rp2)/(rat2+rp2)
    hi=(rp1*(1+e1)*mu)**0.5
    ht1=(rp1*(1+et1)*mu)**0.5
    ht2=(rp2*(1+et2)*mu)**0.5
    hf=(rp2*(1+e2)*mu)**0.5
    
    style.use("dark_background")
    
    theta = linspace(0,2*pi, 1000)
    ri=(hi**2/mu)/(1+e1*cos(theta))
    xi = ri*sin(theta)
    yi = ri*cos(theta)
    plt.plot(xi,yi,color = "orange")

    plt.axis('equal')
    
    beta=linspace(0,2*pi,500)
    xe=6378*cos(beta)
    ye=6378*sin(beta)
    plt.fill(xe,ye, "b")
    
    
    thetat1 = linspace(0, pi, 1000)
    rt1=(ht1**2/mu)/(1+et1*cos(thetat1))
    xt = rt1*sin(thetat1)
    yt = rt1*cos(thetat1)
    plt.plot(xt,yt, color = "yellow", LineStyle = "dotted")
    
    thetat2 = linspace(pi, 2*pi, 1000)
    rt2=(ht2**2/mu)/(1+et2*cos(thetat2))
    xt2 = rt2*sin(thetat2)
    yt2 = rt2*cos(thetat2)
    plt.plot(xt2,yt2, color = "violet", LineStyle = "dotted")
    
    rf=(hf**2/mu)/(1+e2*cos(theta))
    xf = rf*sin(theta)
    yf = rf*cos(theta)
    plt.plot(xf,yf)
    
    
    plt.title("Bi-Elliptical Hohmann Transfer")
    
    plt.show()
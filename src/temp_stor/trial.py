
from numpy import *
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.image as img
def initial_Values(ra1, rp1, ra2, rp2):
    rat = ra2
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
    et=(ra2-rp1)/(ra2+rp1)
    hi=(rp1*(1+e1)*mu)**0.5
    ht=(rp1*(1+et)*mu)**0.5
    hf=(rp2*(1+e2)*mu)**0.5
    
    style.use("dark_background")
    
    theta = linspace(0, 2*pi, 1000)
    ri=(hi**2/mu)/(1+e1*cos(theta))
    xi = ri*sin(theta)
    yi = ri*cos(theta)
    plt.plot(xi,yi,color = "orange")

    plt.axis('equal')
    
    # set_aspect('equal', adjustable='box')
    # matplotlib.axes.Axes.set_xscale(1000,"linear")
    # matplotlib.axes.Axes.set_yscale(1000,"linear")
    
    beta=linspace(0,2*pi,500)
    xe=6378*cos(beta)
    ye=6378*sin(beta)
    plt.fill(xe,ye, "b")
    
    
    thetat = linspace(0, pi, 1000)
    rt=(ht**2/mu)/(1+et*cos(thetat))
    xt = rt*sin(thetat)
    yt = rt*cos(thetat)
    #plt.plot(xt,yt,color = "red", LineStyle = "dotted")
    
    
    rf=(hf**2/mu)/(1+e2*cos(theta))
    xf = rf*sin(theta)
    yf = rf*cos(theta)
    plt.plot(xf,yf,color = "green", LineStyle = "dotted")
    plt.title("Phasing Maneuver")
    
    plt.text(0, 6800,"* Satellite-A")
    
    sma = (ra1 + rp1)/2
    mag_e = (ra1 - rp1)/(ra1 + rp1) 
    slr = sma*(1-mag_e**2)
    plt.text(-slr, 0, "* Satellite-B")
    # plt.axvline(x=0)
    # plt.axhline(y=0)
    
  
# reading the image
    testImage = img.imread('Functions/Assets/Models/hi_res_tex/stars.jpg')
  
# displaying the image
    plt.imshow(testImage)
  
    
    
    plt.show()
    

    
if __name__ == '__main__':
    # apselinerotation(18000, 8000, pi/2)
    # initial_Values(10000,8000, 20000, 15000)
    initial_Values(13600, 6800, 11564, 6800)
    
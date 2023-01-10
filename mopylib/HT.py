from math import *
from numpy import *
from matplotlib.pyplot import*


I = [1, 0, 0]
J = [0, 1, 0]
K = [0, 0, 1]
G = 6.67e-20
major_body = 5.972 * 10**24
r_apoi = 800+6378
r_peri = 480+6378

major_body_mass = major_body * 1
mu = G * major_body_mass


ei = (r_apoi+r_peri)/(r_apoi-r_peri)
mag_h = sqrt(2*mu)*sqrt((r_apoi*r_peri)/(r_peri+r_apoi))
v_peri = mag_h/r_peri
v_apoi = mag_h/r_apoi
print(v_peri,v_apoi)

r_pert = r_peri
r_apot = 16000+6378
et = (r_apot+r_pert)/(r_apot-r_pert)
mag_ht = sqrt(2*mu)*sqrt((r_apot*r_pert)/(r_pert+r_apot))
v_pert = mag_ht/r_pert
v_apot = mag_ht/r_apot
print(v_pert,v_apot)

r_fin = r_apot
v_fin = sqrt(mu/r_fin)
print(v_fin)

del_i = v_pert-v_peri
del_f = v_fin-v_apot
mag_del_i = sqrt (del_i**2)
mag_del_f = sqrt (del_f**2)

del_vtot = mag_del_i+mag_del_f
print(del_vtot)

def circle(t,r):
    x = r*cos(t)
    y = r*sin(t)
    return [x, y]

t=linspace(0,2*pi,1000)

r=((mag_h**2/mu)/(1+(ei)*cos(t)))
[x, y] = circle(t,r)
plot(x,y)


r=((mag_ht**2/mu)/(1+(et)*cos(t)))
[x, y] = circle(t,r)
plot(x,y)


  
r = r_apot
[x, y] = circle(t,r)
fig = figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect('equal',adjustable='box')
plot(x,y)
  


show()





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
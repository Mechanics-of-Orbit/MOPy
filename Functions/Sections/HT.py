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






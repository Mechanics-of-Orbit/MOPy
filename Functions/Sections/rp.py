from math import *
from numpy import *
from numpy.linalg import norm
# rA=[-266.77,3865.8,5426.2]
# vA=[-6.4839,-3.6198,2.4156]
# rB=[-5890.7,-2979.8,1792.2]
# vB=[0.93583,-5.2403,-5.5009]
hA= cross(rA,vA)
mag= norm(hA)
i= rA/norm(rA)
k= hA/norm(hA)
j= cross(k,i)
Q=[i,j,k]
print(Q)
omega=hA/(norm(rA)**2)
r_relative=subtract(rB,rA)
print(r_relative)
v_relative=(subtract(vB,vA))-(cross(omega,r_relative))
print(v_relative)
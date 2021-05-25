from math import *
from numpy import *

order = (input("Enter the order:"))
DCM = [[0.6405, 0.75319, -0.15038],[0.76736, -0.63531, 0.086824],[-0.030154, -0.17101, -0.98481]]
if order=='321':
    theta=-asin(DCM[0][2])
    phi=atan(DCM[1][2]/DCM[2][2])
    si=atan(DCM[0][1]/DCM[0][0])
elif order=='123':
    theta=asin(DCM[2][0])  
    Phi=atan(DCM[2][1]/DCM[2][2])
    si=atan(DCM[1][0]/DCM[0][0])
elif order=='132':
    theta=atan(DCM[2][0]/DCM[0][0])
    phi=atan(DCM[1][2]/DCM[1][1])
    si=-asin(DCM[1][0])
elif order=='312':
    theta=atan(DCM[0][2]/DCM[2][2])
    phi=asin(DCM[1][2])
    si=atan(DCM[1][0]/DCM[1][1])
elif order=='213':
    theta=atan(DCM[2][0]/DCM[2][2])
    phi=-asin(DCM[2][1])
    si=atan(DCM[0][1]/DCM[1][1])
elif order=='231':
    theta=atan(DCM[0][2]/DCM[0][0])
    phi=atan(DCM[2][1]/DCM[1][1])
    si=asin(DCM[0][1])

print(theta)
print(phi)
print(si)
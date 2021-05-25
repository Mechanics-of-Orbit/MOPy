from numpy import *
from math import *
def Rx(phi):
  return matrix([[ 1, 0           , 0           ],
                   [ 0, cos(phi),sin(phi)],
                   [ 0,-sin(phi), cos(phi)]])
  
def Ry(theta):
  return matrix([[ cos(theta), 0,-sin(theta)],
                   [ 0           , 1, 0           ],
                   [sin(theta), 0, cos(theta)]])
  
def Rz(si):
  return matrix([[ cos(si), sin(si), 0 ],
                   [-sin(si), cos(si) , 0 ],
                   [ 0           , 0            , 1 ]])
phi = float(input("Enter the value of Phi(or roll or 1): "))
theta = float(input("Enter the value of Theta(or pitch or 2): "))
si = float(input("Enter the value of si(or yaw or 3): "))
order= (input("Enter the order:"))
if order=='321':
    x = Rx(phi*pi/180)
    y = Ry(theta*pi/180)
    z = Rz(si*pi/180)
    xy = dot(x,y)

    print(dot(xy,z))
elif order == '123':
    x = Rx(phi*pi/180)
    y = Ry(theta*pi/180)
    z = Rz(si*pi/180)
    zy = dot(z,y)

    print(dot(zy,x))
elif order == '213':
    x = Rx(phi*pi/180)
    y = Ry(theta*pi/180)
    z = Rz(si*pi/180)
    zx = dot(z,x)

    print(dot(zx,y))
elif order == '312':
    x = Rx(phi*pi/180)
    y = Ry(theta*pi/180)
    z = Rz(si*pi/180)
    yx = dot(y,x)
    
    print(dot(yx,z))
elif order == '132':
    x = Rx(phi*pi/180)
    y = Ry(theta*pi/180)
    z = Rz(si*pi/180)
    yz = dot(y,z)

    print(dot(yz,x))
elif order == '231':
    x = Rx(phi*pi/180)
    y = Ry(theta*pi/180)
    z = Rz(si*pi/180)
    xz = dot(x,z)

    print(dot(xz,y))
else:
    print('No transformation matrix')
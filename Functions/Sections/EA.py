from math import *
from numpy import *

class EA():

    def RxRyRz(pitch_theta, roll_phi, yaw_si):
        Rx = matrix([[ 1, 0 , 0 ],
                        [ 0, cos(roll_phi),sin(roll_phi)],
                        [ 0,-sin(roll_phi), cos(roll_phi)]])
        
        Ry = matrix([[ cos(pitch_theta), 0,-sin(pitch_theta)],
                        [ 0 ,1, 0],
                        [sin(pitch_theta), 0, cos(pitch_theta)]])
        
        Rz = matrix([[ cos(yaw_si), sin(yaw_si), 0 ],
                        [-sin(yaw_si), cos(yaw_si) , 0 ],
                        [ 0, 0, 1]])
        return [Rx, Ry, Rz]

    def DCMtoEA(DCM, order):
        if order=='321':
            theta=-asin(DCM[0][2])
            phi=atan(DCM[1][2]/DCM[2][2])
            si=atan(DCM[0][1]/DCM[0][0])
        elif order=='123':
            theta=asin(DCM[2][0])  
            phi=atan(DCM[2][1]/DCM[2][2])
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
        return [theta, si, phi]

    def EAtoDCM(theta, si, phi, order):
        [Rx, Ry, Rz] = EA.RxRyRz(theta, si, phi)
        if order=='321':
            RxRy = dot(Rx,Ry)
            return (dot(RxRy,Rz))
        elif order == '123':
            x = Rx(phi*pi/180)
            y = Ry(theta*pi/180)
            z = Rz(si*pi/180)
            zy = dot(z,y)
            return (dot(zy,x))
        elif order == '213':
            x = Rx(phi*pi/180)
            y = Ry(theta*pi/180)
            z = Rz(si*pi/180)
            zx = dot(z,x)
            return (dot(zx,y))
        elif order == '312':
            x = Rx(phi*pi/180)
            y = Ry(theta*pi/180)
            z = Rz(si*pi/180)
            yx = dot(y,x)
            return (dot(yx,z))
        elif order == '132':
            x = Rx(phi*pi/180)
            y = Ry(theta*pi/180)
            z = Rz(si*pi/180)
            yz = dot(y,z)
            return (dot(yz,x))
        elif order == '231':
            x = Rx(phi*pi/180)
            y = Ry(theta*pi/180)
            z = Rz(si*pi/180)
            xz = dot(x,z)
            return (dot(xz,y))
        else:
            return ('No transformation matrix')

order = '321' #input("Enter the order:")
DCM = [[0.6405, 0.75319, -0.15038],[0.76736, -0.63531, 0.086824],[-0.030154, -0.17101, -0.98481]]
print(EA.DCMtoEA(DCM,order))

print(EA.EAtoDCM(8.6489  * 180/pi, 49.619 * 180/pi, -5.039 * 180/pi, order))
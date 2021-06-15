from numpy import * 
from matplotlib.pyplot import *

def ellipse(l, e, theta):
    r = l/(1 - e * cos(theta))
    return r

if __name__ == '__main__':
    theta = linspace(0,2*pi,69420)
    l = 10000
    e = 0.6
    r = ellipse(l, e, theta)

    x = r * cos(theta)
    y = r * sin(theta)
    print(x[2])

    plot(x,y)
    show()
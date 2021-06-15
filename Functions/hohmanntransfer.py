from numpy import *
from matplotlib.pyplot import *
from direct.showbase.ShowBase import ShowBase
from ModelLoader import loadMyModel

from VPCO import CalculateCircularElliptical

from Sections.ellipse import ellipse

class calc():
    def cal(a,e):
        return [a*(1-e**2), a*sqrt(1-e**2)]

    def foci(a, b):
        return sqrt(a**2 - b**2)

class hohmann_method():
    def __init__(self, ra1, rp1, ra2, rp2, majorbody):
        self.ra1 = ra1
        self.rp1 = rp1
        self.ra2 = ra2
        self.rp2 = rp2
        self.majorbody = majorbody

    def coord(self):
        [self.a1, self.a2] = [(rp1+ra1)/2, (rp2+ra2)/2]
        [self.e1, self.e2] = [(ra1-rp1)/(ra1+rp1), (ra2-rp2)/(ra2+rp2)]
        [self.l1, self.b1] = calc.cal(self.a1, self.e1)
        [self.l2, self.b1] = calc.cal(self.a2, self.e2)
        r1 = ellipse(self.l1, self.e1, theta)
        r2 = ellipse(self.l2, self.e1, theta)
        self.at = (rp1+ra2)/2
        self.et = (ra2 - rp1)/(ra2+rp1)
        [self.lt, self.bt] = calc.cal(at, et)
        self.thetat = linspace(0, pi, 10000)
        rt = ellipse(self.lt, self.et, self.thetat)
        ct = calc.foci(at, bt)
        return [r1, r2, rt, ct]
    
class plot(ShowBase):
    def __init__(self, ra1, rp1, ra2, rp2, majorbody):
        super().__init__()
        self.cam.setPos(0, -1000, 0)
        # self.cam.setHpr(0, 90, 0)

        self.bg = self.loader.loadModel("Assets/Models/solar_sky_sphere")
        self.bg.setScale(10000)
        self.bg_tex = self.loader.loadTexture("Assets/Models/hi_res_tex/stars.jpg")
        self.bg.setTexture(self.bg_tex, 1)
        self.bg.reparentTo(self.render)

        load_my_model = loadMyModel()
        model = "earth"
        self.model = load_my_model.body(base, model)
        self.model.setScale(10)
        # self.model.setPos(c/1000000, 0, 0)
        self.model.reparentTo(self.render)

        self.sattl = self.loader.loadModel("Assets/Models/satt")
        self.sattl.setScale(0.05)
        self.sattl.lookAt(self.model)
        self.sattl.reparentTo(self.render)

        cuc = hohmann_method()
        [r1, r2, rt, ct] = cuc.coord()

        self.theta = linspace(-pi,pi,100000)
        self.x1 = (r1 * cos(self.theta))/100
        self.y1 = (r1 * sin(self.theta))/100
        self.z = 0*arange(0,len(self.x))
        self.angle = 0
        self.i = 0

        self.thetat = linspace(0,2*pi,100000)
        self.x1 = (rt * cos(self.thetat))/100
        self.y1 = (rt * sin(self.thetat))/100



if __name__ == '__main__':
    def plotorb(r, theta):
        x = r * cos(theta)
        y = r * sin(theta)
        # fig = figure()
        # ax = fig.add_subplot(111)
        # set_aspect('equal', adjustable='box')
        plot(x,y)

    [rp1, ra1] = [6378+480, 6378+480]
    [rp2, ra2] = [6378+16000, 6378+16000]
    [a1, a2] = [(rp1+ra1)/2, (rp2+ra2)/2]
    [e1, e2] = [(ra1-rp1)/(ra1+rp1), (ra2-rp2)/(ra2+rp2)]

    [l1, b1] = calc.cal(a1, e1)
    [l2, b1] = calc.cal(a2, e2)

    theta = linspace(0, 2*pi, 10000)
    r1 = ellipse(l1, e1, theta)
    r2 = ellipse(l2, e1, theta)

    at = (rp1+ra2)/2
    et = (ra2 - rp1)/(ra2+rp1)
    [lt, bt] = calc.cal(at, et)
    thetat = linspace(0, pi, 10000)
    rt = ellipse(lt, et, thetat)
    ct = calc.foci(at, bt)

    plotorb(r1, theta)
    plotorb(r2, theta)
    plotorb(rt, thetat)
    show()

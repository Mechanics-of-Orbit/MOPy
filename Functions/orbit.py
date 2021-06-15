from panda3d.core import loadPrcFileData

confVars = """
win-size 1280 720
window-title Orbit
show-frame-rate-meter true
"""

loadPrcFileData("", confVars)

from numpy import *

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from Sections.ellipse import ellipse
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from ModelLoader import loadMyModel

class pandaorbit(ShowBase):
    def __init__(self, r, c):
        super().__init__()

        self.cam.setPos(0, -1000, 0)
        # self.cam.setHpr(0, 90, 0)

        self.bg = self.loader.loadModel("Assets/Models/solar_sky_sphere")
        self.bg.setScale(10000)
        self.bg_tex = self.loader.loadTexture("Assets/Models/hi_res_tex/stars.jpg")
        self.bg.setTexture(self.bg_tex, 1)
        self.bg.reparentTo(self.render)

        load_my_model = loadMyModel()
        model = "mars"
        self.model = load_my_model.body(base, model)
        self.model.setScale(10)
        # self.model.setPos(c/1000000, 0, 0)
        self.model.reparentTo(self.render)

        self.sattl = self.loader.loadModel("Assets/Models/satt")
        self.sattl.setScale(0.05)
        self.sattl.lookAt(self.model)
        self.sattl.reparentTo(self.render)
        

        self.theta = linspace(0,2*pi,100000)
        self.x = (r * cos(self.theta))/100
        self.y = (r * sin(self.theta))/100
        self.z = 0*arange(0,len(self.x))
        self.angle = 0
        self.i = 0

        
        self.taskMgr.add(self.orbit, "orbit")
        
    
    def orbit(self, task):
        dt = globalClock.getDt()
        
        self.sattl.setPos(self.x[self.i],0, self.y[self.i])
        # self.cam.setPos(self.x[self.i],0, self.y[self.i])
        self.cam.lookAt(self.sattl)
        
        #self.model.setHpr(self.angle, 0 ,0)
        #self.sattl.setHpr(0, self.angle, 0)

        if self.i < 99000:
            self.i += 1000
        else:
            self.i = 0
        self.angle += 1

        return task.cont

if __name__ == '__main__':
    theta = linspace(0,2*pi,100000)
    a = 20000
    e = 0
    l = a*(1-e**2)
    r = ellipse(l, e, theta)
    b = a*sqrt(1-e**2)
    c = a**2 - b**2
    print(a*(a-e))
    play = pandaorbit(r,c)
    play.run()

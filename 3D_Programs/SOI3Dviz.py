from panda3d.core import loadPrcFile
loadPrcFile("Sections/SoI/config.prc")
from soi import *

from direct.showbase.ShowBase import ShowBase
# from panda3d.core import NodePath
from direct.actor.Actor import Actor


[rSOI, rSOIMiB] = SoI("Sun", "Earth")

class SOI(ShowBase):
    def __init__(self, planet):
        super().__init__()

        self.camera.setPos(0,-700,0)
        
        self.stars = self.loader.loadModel("Assets/solar_sky_sphere")
        self.stars.setScale(500)
        self.stars.reparentTo(render)
        self.stars_tex = loader.loadTexture("Assets/hi_res_tex/a_stars.jpg")
        self.stars.setTexture(self.stars_tex,1)

        self.planet_name = planet
        self.dire = "Assets\hi_res_tex" + r'\a_'
        self.ComDir = self.dire + self.planet_name + ".jpg"
        self.MinorBody = self.loader.loadModel("Assets/planet_sphere")
        self.MinorBody.setScale(2)
        self.MinorBody_tex = loader.loadTexture(self.ComDir)
        self.MinorBody.setTexture(self.MinorBody_tex, 1)
        self.MinorBody.reparentTo(render)

        self.soi_m = self.loader.loadModel("Assets/planet_sphere")
        self.soi_m.setScale(2*rSOIMiB)
        self.soi_m.setTransparency(1)
        self.soi_m.setColor(1,1,1,.25)
        self.soi_m.reparentTo(self.MinorBody)






soi = SOI("earth_daymap")
soi.run()

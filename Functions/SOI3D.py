from panda3d.core import loadPrcFileData
confVars = """
win-size 1280 720
window-title Sphere of Influence
show-frame-rate-meter true
show-scene-graph-analyzer-meter true
"""
loadPrcFileData("", confVars)

from direct.showbase.ShowBase import ShowBase
from Functions.ModelLoader import loadMyModel
from Functions.Sections.soi import SOICalc
from Functions.Sections.DB.call_database import call

class SOI3D(ShowBase):
    def __init__(self, MinorBody):
        super().__init__()

        scale = 0.001

        #Loading the BG Stars
        self.stars = self.loader.loadModel("Functions/Assets/Models/solar_sky_sphere")
        self.stars_tex = self.loader.loadTexture("Functions/Assets/Models/hi_res_tex/stars.jpg")
        self.stars.setTexture(self.stars_tex,1)
        
        self.stars.reparentTo(render)



        # Loading the Minor Body
        [rSOI, rSOIMiB] = SOICalc(MinorBody)
        PlanetLoader = loadMyModel()
        self.MinorBodyModel = PlanetLoader.body(base, MinorBody)
        [self.MinorBodyRadius, a] = call.data(MinorBody, "radius")
        # print(type(self.MinorBodyRadius))
        self.MinorBodyModel.setScale(scale*self.MinorBodyRadius)
        self.MinorBodyModel.reparentTo(render)
        
        self.stars.setScale(0.004*rSOI)
        self.cam.setPos(0, -0.004*rSOI,0)

        # Sphere Of Influence
        self.SOIModel = PlanetLoader.body(base, "white")
        self.SOIModel.setScale(scale * rSOI)
        self.SOIModel.setTransparency(1)
        self.SOIModel.setColor(1, 1, 1, 0.1)
        self.SOIModel.reparentTo(render)


if __name__ == '__main__':
    viz = SOI3D("Uranus")
    viz.run()


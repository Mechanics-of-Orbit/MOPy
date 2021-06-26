from panda3d.core import loadPrcFileData
confVars = """
win-size 1280 720
window-title Sphere of Influence
show-frame-rate-meter true
show-scene-graph-analyzer-meter true
"""
loadPrcFileData("", confVars)

from direct.showbase.ShowBase import ShowBase
from ModelLoader import loadMyModel

class SOI(ShowBase):
    def __init__(self, Minor_Body, rSOI, rSOIMiB):
        super().__init__()

        self.stars = self.loader.loadModel("Assets/Models/solar_sky_sphere")
        self.stars.setScale(10000)
        self.stars.reparentTo(render)
        self.stars_tex = loader.loadTexture("Functions/Assets/Models/hi_res_tex/stars.jpg")
        self.stars.setTexture(self.stars_tex,1)

        load_my_model = loadMyModel()
        self.Minor_Body_Model = load_my_model.body(base, Minor_Body)
        self.Minor_Body_Model.setScale(2)
        self.Minor_Body_Model.reparentTo(render)

        load_my_model = loadMyModel()
        self.SOI_Model = load_my_model.body(base, "white")
        self.SOI_Model.setScale(5)
        self.SOI_Model.setTransparency(1)
        self.SOI_Model.setColor(1,1,1,0.1)
        self.SOI_Model.reparentTo(render)


        self.cam.setPos(0,-100,0)

if __name__ == '__main__':
    #[rSOI, rSOIMiB] = SoI("Sun", "Earth")
    soi = SOI("earth",800000, 140)
    soi.run()        

        

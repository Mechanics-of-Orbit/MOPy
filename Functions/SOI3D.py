from panda3d.core import loadPrcFileData
confVars = """
win-size 1280 720
window-title Sphere of Influence
show-frame-rate-meter true
show-scene-graph-analyzer-meter true
"""
loadPrcFileData("", confVars)

from direct.showbase.ShowBase import ShowBase


if __name__ == '__main__':
    from ModelLoader import loadMyModel
    from Sections.DB.call_database import call
else:
    from Functions.Sections.DB.call_database import call
    from Functions.ModelLoader import loadMyModel

class SOI(ShowBase):
    def __init__(self, Minor_Body, rSOI, rSOIMiB):
        super().__init__()

        self.model_scale = 1e-6
        minor_body_radius = call.data(Minor_Body,'radius')[0]/2
        

        self.stars = self.loader.loadModel("Functions/Assets/Models/solar_sky_sphere")
        self.stars.setScale(10000)
        self.stars.reparentTo(render)
        self.stars_tex = loader.loadTexture("Functions/Assets/Models/hi_res_tex/stars.jpg")
        self.stars.setTexture(self.stars_tex,1)

        load_my_model = loadMyModel()
        self.Minor_Body_Model = load_my_model.body(base, Minor_Body)
        self.Minor_Body_Model.setScale(minor_body_radius)
        self.Minor_Body_Model.reparentTo(render)

        load_my_model = loadMyModel()
        self.SOI_Model = load_my_model.body(base, "white")
        self.SOI_Model.setScale(rSOI)
        self.SOI_Model.setTransparency(1)
        self.SOI_Model.setColor(1,1,1,0.1)
        self.SOI_Model.reparentTo(render)


        self.cam.setPos(0,-rSOI,0)

if __name__ == '__main__':
    #[rSOI, rSOIMiB] = SoI("Sun", "Earth")
    soi = SOI("Earth",800000, 140)
    soi.run()        

        

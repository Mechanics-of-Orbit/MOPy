from panda3d.core import loadPrcFile
loadPrcFile("config/config.prc")
#from Sections.soi import SoI

from direct.showbase.ShowBase import ShowBase
# from panda3d.core import NodePath
from direct.actor.Actor import Actor





class SOI(ShowBase):
    def __init__(self, Minor_Body, rSOI, rSOIMiB):
        super().__init__()

        
        self.stars = self.loader.loadModel("Assets/Models/solar_sky_sphere")
        self.stars.setScale(10000)
        self.stars.reparentTo(render)
        self.stars_tex = loader.loadTexture("Assets/Models/hi_res_tex/stars.jpg")
        self.stars.setTexture(self.stars_tex,1)

        self.Minor_Body_name = Minor_Body
        self.dire = "Assets\Models\hi_res_tex" + r'\a_'
        self.ComDir = self.dire + self.Minor_Body_name + ".jpg"
        self.MinorBody = self.loader.loadModel("Assets/Models/planet_sphere")
        self.MinorBody.setScale(2)
        self.MinorBody_tex = loader.loadTexture(self.ComDir)
        self.MinorBody.setTexture(self.MinorBody_tex, 1)
        self.MinorBody.reparentTo(render)

        self.soi_m = self.loader.loadModel("Assets/Models/planet_sphere")
        self.soi_m.setScale(2*rSOIMiB)
        self.soi_m.setTransparency(1)
        self.soi_tex = loader.loadTexture(r'Assets/Models/hi_res_tex/white.jpg')
        self.soi_m.setTexture(self.soi_tex,1)
        self.soi_m.setColor(1,1,1,.1)
        self.soi_m.reparentTo(self.MinorBody)

        self.cam.setPos(0,-2000,0)

if __name__ == '__main__':
    #[rSOI, rSOIMiB] = SoI("Sun", "Earth")
    soi = SOI("earth",800000, 140)
    soi.run()
 
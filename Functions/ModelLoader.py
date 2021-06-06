from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from common import Common
# from panda3d.core import Loader, NodePath

class loadMyModel():
    def __init__(self):
        self.dire = r'Assets\Models\hi_res_tex\a_'
        self.ComDir = self.dire + "earth_daymap" + ".jpg"

        self.modelObject = Common.game.loader.loadModel("Assets/Models/planet_sphere")
        self.modelObject_tex = Common.game.loader.loadTexture(self.ComDir)
        self.modelObject.setTexture(self.modelObject_tex,1)


if __name__ == '__main__':
    abc = loadMyModel("earth_daymap")
    abc.run()

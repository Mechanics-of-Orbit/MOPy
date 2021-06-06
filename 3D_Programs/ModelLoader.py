from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Camera

class loadMyModel():
    def __init__(self, model):
        super().__init__()

        self.dire = r'Assets\Models\hi_res_tex\a_'
        self.modelName = model
        self.ComDir = self.dire + self.modelName + ".jpg"

        self.ModelLoad = self.loader.loadModel("Assets/Models/planet_sphere")
        self.ModelLoad = self.loader.loadTexture(self.ComDir)

        self.ModelLoad.reparentTo(render)

        # return self.ModelLoad

if __name__ == '__main__':
    abc = loadMyModel("earth_daymap")
    abc.run()

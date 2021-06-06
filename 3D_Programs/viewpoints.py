from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Camera

class MyGame(ShowBase):
    def __init__(self):
        super().__init__()

        self.land = loader.loadModel("models/environment")
        self.land.reparentTo(render)
        self.land.setPos(0,0,0)

        self.model1 = Actor("Assests/Models/planet_sphere")
        self.model1.reparentTo(render)
        self.model1.setScale(2)
        self.model1.setPos(10, 12, 0)


        self.model2 = Actor("models/panda")
        self.model2.reparentTo(render)
        self.model2.setScale(.2)
        self.model2.setPos(0, 0, 0)

        self.my_cam1 = Camera("cam1")
        self.my_camera1 = render.attachNewNode(self.my_cam1)
        self.my_camera1.setName("camera1")
        self.my_camera1.setPos(0,20,0)
        self.my_camera1.lookAt(self.model2)

        self.my_cam2 = Camera("cam2")
        self.my_camera2 = render.attachNewNode(self.my_cam2)
        self.my_camera2.setName("camera2")
        self.my_camera2.setPos(0,20,0)
        self.my_camera2.lookAt(self.model1)
        self.my_camera2.setH(45)

        self.my_cam3 = Camera("cam3")
        self.my_camera3 = render.attachNewNode(self.my_cam3)
        self.my_camera3.setName("camera3")
        self.my_camera3.setPos(0,10,0)
        self.my_camera3.lookAt(self.land)
        

        self.dr = base.camNode.getDisplayRegion(0)
        self.dr.setActive(0) # Or leave it (dr.setActive(1))

        window = self.dr.getWindow()
        self.dr1 = window.makeDisplayRegion(0, 0.5, 0, 1)
        self.dr1.setSort(self.dr.getSort())
        self.dr2 = window.makeDisplayRegion(0.5, 1, 0, 1)
        self.dr2.setSort(self.dr.getSort())

        self.dr3 = window.makeDisplayRegion(0.8, 0.9, 0.2, 0.4)
        self.dr3.setSort(self.dr.getSort())

        self.dr1.setCamera(self.my_camera1)
        self.dr2.setCamera(self.my_camera2)
        self.dr3.setCamera(self.my_camera3)


game = MyGame()
game.run()
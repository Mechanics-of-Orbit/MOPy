from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Camera

class MyGame(ShowBase):
    def __init__(self):
        super().__init__()

        self.my_cam1 = Camera("cam1")
        self.my_camera1 = render.attachNewNode(self.my_cam1)
        self.my_camera1.setName("camera1")

        
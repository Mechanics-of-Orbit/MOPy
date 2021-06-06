from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Camera

class MyGame(ShowBase):
    def __init__(self, model):
        super().__init__()
        

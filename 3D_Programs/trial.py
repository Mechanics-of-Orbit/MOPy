from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
import ModelLoader as ml

class trial(ShowBase):
    def __init__(self):
        super().__init__()

        self.Earth = ml.loadMyModel("earth_daymap")
        self.Earth.reparentTo(render)

trialrun = trial()
trial.run()

from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from ModelLoader import loadMyModel
from common import Common

class trial(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        Common.game = self

        Earth = loadMyModel("earth_daymap")
        Earth.reparentTo(render)

trialrun = trial()
trial.run()

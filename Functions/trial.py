from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from ModelLoader import loadMyModel

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        load_my_model = loadMyModel()
        model = "earth_daymap"
        self.main_model = load_my_model.body(base, model)
        self.main_model.reparentTo(render)

        self.solar_sky = load_my_model.solar_sky(base,2000)
        self.solar_sky.reparentTo(render)


app = MyApp()
app.run()
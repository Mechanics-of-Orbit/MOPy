from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from panda3d.core import NodePath
from panda3d.core import loadPrcFileData
from panda3d.core import *



class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)


        # self.disableMouse()


        # properties = WindowProperties()
        # properties.setSize(1000, 750)
        # properties.setCursorHidden(True) 
        # self.win.requestProperties(properties)


        self.stars = self.loader.loadModel("Assets/Models/solar_sky_sphere")
        self.stars.setScale(10000000)
        self.stars.reparentTo(render)
        self.stars_tex = loader.loadTexture("Assets/Models/hi_res_tex/stars.jpg")
        self.stars.setTexture(self.stars_tex,1)


        self.model = self.loader.loadModel("Assets/Models/planet_sphere")
        self.model.setScale(20000)
        self.model.reparentTo(render)
        self.model_tex = loader.loadTexture("Assets/Models/hi_res_tex/a_earth_daymap.jpg")
        self.model.setTexture(self.model_tex,1)

        
        self.parentnode = render.attachNewNode('camparent')
        self.parentnode.reparentTo(self.model) # inherit transforms
        self.parentnode.setEffect(CompassEffect.make(render)) # NOT inherit rotation
        
        
       
        keyMap = {"a":0, "d":0, "w":0, "s":0}

        self.cam.reparentTo(self.parentnode)
        self.cam.lookAt(self.parentnode)
        self.cam.setPos(0,-1000,0)
        

        def setKey(key, value):
	        keyMap[key] = value

        def cameraMovement(task):
            if (keyMap["a"]!=0):
                self.parentnode.setH(self.parentnode.getH()-200 * globalClock.getDt())
            if (keyMap["d"]!=0):
                self.parentnode.setH(self.parentnode.getH()+200 * globalClock.getDt())
            if (keyMap["w"]!=0):
                self.parentnode.setP(self.parentnode.getP()-200 * globalClock.getDt())
            if (keyMap["s"]!=0):
                self.parentnode.setP(self.parentnode.getP()+200 * globalClock.getDt())
            return task.cont


        taskMgr.add(cameraMovement, 'cameraMovement')


        self.accept('wheel_up', lambda : self.cam.setY(self.cam.getY()+1500 * globalClock.getDt()))
        self.accept('wheel_down', lambda : self.cam.setY(self.cam.getY()-1500 * globalClock.getDt()))

   
        self.accept('a', setKey, ["a",1])
        self.accept('a-up', setKey, ["a",0])
        self.accept('d', setKey, ["d",1])
        self.accept('d-up', setKey, ["d",0])
        self.accept('w', setKey, ["w",1])
        self.accept('w-up', setKey, ["w",0])
        self.accept('s', setKey, ["s",1])
        self.accept('s-up', setKey, ["s",0])



game = Game()
game.run()
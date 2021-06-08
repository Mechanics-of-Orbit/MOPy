from panda3d.core import loadPrcFile
loadPrcFile("Sections/SoI/config.prc")
from panda3d.core import *


from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath
from direct.actor.Actor import Actor
from direct.task import Task


# global vars for camera rotation
heading = 0
pitch = 0

class Game(ShowBase):
    def __init__(self):
        super().__init__()

        # self.cam.setPos(0,-5000,0)

        self.stars = self.loader.loadModel("Assets/Models/solar_sky_sphere")
        self.stars.setScale(10000000)
        self.stars.reparentTo(render)
        self.stars_tex = loader.loadTexture("Assets/Models/hi_res_tex/stars.jpg")
        self.stars.setTexture(self.stars_tex,1)

        self.model = self.loader.loadModel("Assets/Models/planet_sphere")
        self.model.setScale(20000)
        self.model_tex = loader.loadTexture("Assets/Models/hi_res_tex/a_earth_daymap.jpg")
        self.model.setTexture(self.model_tex,1)
        self.model.reparentTo(render)



        # dummy node
        self.parentnode = render.attachNewNode('camparent')
        self.parentnode.reparentTo(self.model) 
        self.parentnode.setEffect(CompassEffect.make(render))

        # camera
        self.cam.reparentTo(self.parentnode)
        self.cam.lookAt(self.parentnode)
        self.cam.setY(-1000) # camera distance from model

        
        # camera zooming
        self.accept('wheel_up', lambda : self.cam.setY(self.cam.getY()+1500 * globalClock.getDt()))
        self.accept('wheel_down', lambda : self.cam.setY(self.cam.getY()-1500 * globalClock.getDt()))

       


    # camera rotation task
        def thirdPersonCameraTask(task):
            global heading
            global pitch
            
            md = base.win.getPointer(0)
                
            x = md.getX()
            y = md.getY()

            if base.win.movePointer(0, 300, 300):
                heading = heading - (x - 300) * 0.5
                pitch = pitch - (y - 300) * 0.5
            
            self.parentnode.setHpr(heading, pitch,0)
            
            
            return task.cont

        self.taskMgr.add(thirdPersonCameraTask, 'thirdPersonCameraTask')
    

        



game = Game()
game.run()
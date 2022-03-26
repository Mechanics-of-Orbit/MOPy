# from panda3d.core import loadPrcFile
# loadPrcFile("config/conf.prc")

# from direct.showbase.ShowBase import ShowBase
# from ModelLoader import loadMyModel

# class MyApp(ShowBase):

#     def __init__(self):
#         ShowBase.__init__(self)

#         load_my_model = loadMyModel()
#         model = "earth"
#         self.main_model = load_my_model.body(base, model)
#         self.main_model.reparentTo(render)

#         self.cam.setPos(0,-100,0)
#         # self.sol_sky = load_my_model.solar_sky(base)
#         # self.sol_sky.reparentTo(render)


# app = MyApp()
# app.run()

# [a, b] = [[1, 2, 3, 4], [5, 6, 7, 8]]
import numpy as np
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + 2.5*np.array(b)
print(type(a))
print(b*4)
print(np.sin(c))
print(c[1])
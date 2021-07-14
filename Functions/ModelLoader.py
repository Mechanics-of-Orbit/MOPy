class loadMyModel():
    def __init__(self):
        pass

    def body(self, base, model):
        ob = base.loader.loadModel(r"Functions\Assets\Models\planetsphere")
        ComDir = r"Functions\Assets\Models\hi_res_tex\a_" + model + ".jpg"
        ob_tex = base.loader.loadTexture(ComDir)
        ob.setTexture(ob_tex)
        return ob
    
    def astronaut(self, base, model):
        ob = base.Actor(model)
    
    def solar_sky(self, base):
        sol_sky = base.loader.loadModel(r"Functions\Assets\Models\solar_sky_sphere")
        sol_sky = base.loader.loadTexture(r"Functions\Assets\Models\hi_res_tex\stars.jpg")
        



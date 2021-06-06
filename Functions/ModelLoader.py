class loadMyModel():
    def __init__(self):
        pass

    def body(self, base, model):
        ob = base.loader.loadModel("Assets\Models\planet_sphere")
        ComDir = r'Assets\Models\hi_res_tex\a_' + model + ".jpg"
        ob_tex = base.loader.loadTexture(ComDir)
        ob.setTexture(ob_tex)
        return ob
    
    def astronaut(self, base, model):
        ob = base.Actor(model)
    
    def solar_sky(self, base, scale):
        sol_sky = base.loader.loadModel("Assests\Models\solar_sky_sphere")
        sol_sky = base.loader.loadTexture("Assests\Models\hi_res_tex\stars.jpg")
        sol_sky.setScale(scale)



import numpy as np
import GlobalConstants as GCs

class OrbitalValues:
    """The initiate the variables and calculate all the rest of the values related to the orbit based on the input.
    This take the given inputs and evaluates if the given information is enough to calculate the all the required orbital values. 
    If not, it will return an error.
    
    If it does you can calculate other operations in this class.
    
    Args:
        major_body (String): Name of the Major Body of the Orbit
        radiusOfApogee (float, optional): Radius of Apogee of the Orbit. Defaults to empty string.
        radiusOfPerigee (float, optional): Radius of Perigee of the Orbit. Defaults to empty string.
        semi_major_axis (float, optional): Semi Major Axis of the Orbit. Defaults to empty string.
        eccentricity (Float, optional): Eccentricity of the Orbit. Defaults to empty string.
    """
    def __init__(self, major_body, radiusOfApogee = '', radiusOfPerigee = '', semi_major_axis='', eccentricity=''): #todo np.nan is not working need to fix it temp fix used empty string
        self.major_body = major_body
        self.major_body_mass = 1
        self.radiusOfApogee = radiusOfApogee
        self.radiusOfPerigee = radiusOfPerigee
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        OrbitalValues.calculate_rest(self)        
    
    def calculate_orbital_constants(self):
        self.gravitational_constant = GCs.NEWTONGRAVITATIONALCONSTANT * self.major_body_mass
        self.semi_latus_rectum = self.semi_major_axis*(1-self.eccentricity**2)
        self.specific_angular_momentum = (self.radiusOfPerigee*(1+self.eccentricity)*self.gravitational_constant)**0.5
        self.orbital_time_period = np.sqrt(((4*np.pi**2)/self.gravitational_constant)*self.semi_major_axis**3)
        self.mean_motion = self.orbital_time_period/(2*np.pi)
        self.specific_mechanical_energy = -self.gravitational_constant/(2* self.semi_major_axis)
        return self.mean_motion, self.orbital_time_period, self.specific_angular_momentum, self.specific_mechanical_energy, self.semi_latus_rectum
    
    def calculate_rest(self):
        print(self.radiusOfApogee and self.radiusOfPerigee != '')
        if self.radiusOfApogee and self.radiusOfPerigee != '':
            print("hello")
            self.semi_major_axis = (self.radiusOfPerigee + self.radiusOfApogee)/2
            self.eccentricity = (self.radiusOfApogee - self.radiusOfPerigee)/ \
                                (self.radiusOfApogee + self.radiusOfPerigee)
        elif self.semi_major_axis and self.eccentricity != '':
            self.radiusOfPerigee = self.semi_major_axis * (1 - self.eccentricity)
            self.radiusOfApogee  = self.semi_major_axis * (1 + self.eccentricity)
            
        elif self.semi_major_axis and self.radiusOfApogee != '':
            self.radiusOfPerigee = 2*self.semi_major_axis - self.radiusOfApogee
            self.eccentricity = (self.radiusOfApogee - self.radiusOfPerigee)/ \
                                (self.radiusOfApogee + self.radiusOfPerigee)
                          
        OrbitalValues.calculate_orbital_constants(self)
        
    def caculate_orbital_values(self):
        orbital_values = {"SemiMajorAxis": self.semi_major_axis, "Eccentricity": self.eccentricity,
                          "RadiusOfPerigee": self.radiusOfPerigee, "RadiusOfApogee": self.radiusOfApogee,
                          "MeanMotion": self.mean_motion, "TimePeriod": self.orbital_time_period, 
                          "SpecificAngularMomentum": self.specific_angular_momentum, "SpecificMechanicalEnergy":self.specific_mechanical_energy, 
                          "SemiLatusRectum":self.semi_latus_rectum
                          }
        
        return orbital_values
    
    def test_2(self):
        self.a = "Hallo"
        return self.a
    
    def test_3(self):
        b = OrbitalValues.test_2(self)
        
    def test(self):
        print('Hello')
        print(GCs.NEWTONGRAVITATIONALCONSTANT)
        OrbitalValues.test_3(self)
        print(self.a)

if __name__ == '__main__':
    # test = OrbitalValues("Earth", radiusOfApogee = 20000, radiusOfPerigee = 10000)
    test = OrbitalValues("Earth", semi_major_axis=20000, eccentricity=0.4)
    orbital_values = test.caculate_orbital_values()
    print(orbital_values)
    # print(GCs.IVECTOR)
import numpy as np
import constants.GlobalConstants as GCs


class OrbitalValues:
    """The initiate the variables and calculate all the rest of the values related to the orbit based on the input.
    This take the given inputs and evaluates if the given information is enough to calculate the all the required orbital values. 
    If not, it will return an error.
    
    ### !!!Enter any of the two values only to avoid over constrained situation!!!
    
    If it does you can calculate other operations in this class.
    
    Args:
        major_body (String): Name of the Major Body of the Orbit
        radiusOfApogee (float, optional): Radius of Apogee of the Orbit. Defaults to empty string.
        radiusOfPerigee (float, optional): Radius of Perigee of the Orbit. Defaults to empty string.
        semi_major_axis (float, optional): Semi Major Axis of the Orbit. Defaults to empty string.
        eccentricity (Float, optional): Eccentricity of the Orbit. Defaults to empty string.
    """
    def __init__(self, major_body, radius_of_apogee = None, radius_of_perigee = None, semi_major_axis=None, eccentricity=None):
        self.major_body = major_body
        self.major_body_mass = 1 #todo: link to database
        self.radius_of_apogee = radius_of_apogee
        self.radius_of_perigee = radius_of_perigee
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        OrbitalValues.calculate_rest(self)        
    
    def calculate_orbital_constants(self):
        self.gravitational_constant = GCs.NEWTON_GRAVITATIONAL_CONSTANT * self.major_body_mass
        self.semi_latus_rectum = self.semi_major_axis*(1-self.eccentricity**2)
        self.specific_angular_momentum = (self.radius_of_perigee*(1+self.eccentricity)*self.gravitational_constant)**0.5
        self.orbital_time_period = np.sqrt(((4*np.pi**2)/self.gravitational_constant)*self.semi_major_axis**3)
        self.mean_motion = self.orbital_time_period/(2*np.pi)
        self.specific_mechanical_energy = -self.gravitational_constant/(2* self.semi_major_axis)
        return self.mean_motion, self.orbital_time_period, self.specific_angular_momentum, self.specific_mechanical_energy, self.semi_latus_rectum
    
    def calculate_rest(self):
        if self.radius_of_apogee and self.radius_of_perigee != None:
            self.semi_major_axis = (self.radius_of_perigee + self.radius_of_apogee)/2
            self.eccentricity = (self.radius_of_apogee - self.radius_of_perigee)/ \
                                (self.radius_of_apogee + self.radius_of_perigee)
        elif self.semi_major_axis and self.eccentricity != None:
            self.radius_of_perigee = self.semi_major_axis * (1 - self.eccentricity)
            self.radius_of_apogee  = self.semi_major_axis * (1 + self.eccentricity)
            
        elif self.semi_major_axis and self.radius_of_apogee != None:
            self.radius_of_perigee = 2*self.semi_major_axis - self.radius_of_apogee
            self.eccentricity = (self.radius_of_apogee - self.radius_of_perigee)/ \
                                (self.radius_of_apogee + self.radius_of_perigee)
        elif self.semi_major_axis and self.radius_of_perigee != None:
            self.radius_of_apogee = 2*self.semi_major_axis - self.radius_of_perigee
            self.eccentricity = (self.radius_of_apogee - self.radius_of_perigee)/ \
                                (self.radius_of_apogee + self.radius_of_perigee)
        elif self.eccentricity and self.radius_of_apogee != None:
            self.radius_of_perigee = self.radius_of_apogee * ((1 - self.eccentricity)/(1 + self.eccentricity))
            self.semi_major_axis = (self.radius_of_perigee + self.radius_of_apogee)/2
        elif self.eccentricity and self.radius_of_perigee != None:
            self.radius_of_apogee = self.radius_of_perigee * ((1 + self.eccentricity)/(1 - self.eccentricity))
            self.semi_major_axis = (self.radius_of_perigee + self.radius_of_apogee)/2        
                          
        OrbitalValues.calculate_orbital_constants(self)
        
    def caculate_orbital_values(self):
        orbital_values = {"SemiMajorAxis": self.semi_major_axis, "Eccentricity": self.eccentricity,
                          "RadiusOfPerigee": self.radius_of_perigee, "RadiusOfApogee": self.radius_of_apogee,
                          "MeanMotion": self.mean_motion, "TimePeriod": self.orbital_time_period, 
                          "SpecificAngularMomentum": self.specific_angular_momentum, "SpecificMechanicalEnergy":self.specific_mechanical_energy, 
                          "SemiLatusRectum":self.semi_latus_rectum
                          }
        
        return orbital_values
    
    def calculate_velocity_at_point(self, radius='',angle=''):
        if angle != '':
            radius = ((self.specific_angular_momentum**2/self.gravitational_constant)/(1+(self.eccentricity)*np.cos(angle)))

        velocity = np.sqrt((2*self.gravitational_constant/radius)-(self.gravitational_constant/self.semi_major_axis))

        return velocity
    
    def test_2(self):
        self.a = "Hallo"
        return self.a
    
    def test_3(self):
        b = OrbitalValues.test_2(self)
        
    def test(self):
        print('Hello')
        print(GCs.NEWTON_GRAVITATIONAL_CONSTANT)
        OrbitalValues.test_3(self)
        print(self.a)

if __name__ == '__main__':
    import pandas as pd
    # test = OrbitalValues("Earth", radiusOfApogee = 20000, radiusOfPerigee = 10000)
    orbit_1 = OrbitalValues("Earth", semi_major_axis=20000, eccentricity=0.4)
    # orbit_2 = OrbitalValues("Earth", semi_major_axis=20000, radius_of_apogee=28000)
    # orbit_3 = OrbitalValues("Earth", semi_major_axis=20000, radius_of_perigee=12000)
    # orbit_4 = OrbitalValues("Earth", eccentricity=0.4, radius_of_apogee=28000)
    # orbit_5 = OrbitalValues("Earth", eccentricity=0.4, radius_of_perigee=12000)
    # orbit_6 = OrbitalValues("Earth", radius_of_perigee=12000, radius_of_apogee=28000)
    # orbital_values = [orbit_1.caculate_orbital_values(), orbit_2.caculate_orbital_values(), orbit_3.caculate_orbital_values(), orbit_4.caculate_orbital_values(), orbit_5.caculate_orbital_values(), orbit_6.caculate_orbital_values()]
    orbital_values = [orbit_1.caculate_orbital_values()]
    orbital_values_df = pd.DataFrame.from_dict(orbital_values)
    pd.set_option('display.max_columns', None)
    # orbital_values_df.head()
    print(orbital_values_df.T)
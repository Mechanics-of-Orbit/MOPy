import numpy as np

import constants.GlobalConstants as GCs

class OrbitalElements():
    def __init__(self, major_body, position_vector = None, velocity_vector = None, semi_major_axis=None, \
                 eccentricity=None, inclination=None, RAAN=None, argument_of_periapsis=None, true_anomaly=None):
        self.major_body = major_body
        self.major_body_mass = 5.972e24 #kg #todo: link to database
        self.position_vector = position_vector
        self.velocity_vector = velocity_vector
        self.position_magnitude = self.radius_of_orbit = np.linalg.norm(self.position_vector)
        self.velocity_magnitude = self.velocity = np.linalg.norm(self.velocity_vector)
        self.orbital_elements_values_dict = {}
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        self.G = GCs.NEWTON_GRAVITATIONAL_CONSTANT
        self.I = GCs.IVECTOR
        self.J = GCs.JVECTOR
        self.K = GCs.KVECTOR
        self.gravitational_constant = GCs.NEWTON_GRAVITATIONAL_CONSTANT * self.major_body_mass
    
    def calculate_angular_momentum(self):
        self.angular_momentum_vector = np.cross(self.position_vector, self.velocity_vector)
        self.angular_momentum = np.linalg.norm(self.angular_momentum_vector)
        self.orbital_elements_values_dict["AngularMomentum"] = self.angular_momentum
    
    def calculate_node_line_vector(self):
        self.n_vector = np.cross(self.K, self.angular_momentum_vector)
        self.n_vector_magnitude = np.linalg.norm(self.n_vector)
        # self.orbital_elements_names["NodalVector"] = self.n_vector
    
    def calculate_eccentricity(self):
        self.eccentricity_vector = (np.multiply((self.velocity_magnitude**2-self.gravitational_constant/self.position_magnitude),self.position_vector)-\
                                    np.multiply(np.dot(self.position_vector, self.velocity_vector), self.velocity_vector))/self.gravitational_constant
        self.eccentricity = np.linalg.norm(self.eccentricity_vector)
        self.orbital_elements_values_dict["Eccentricity"] = self.eccentricity
    
    def calculate_semi_major_axis(self):
        self.semi_major_axis = 1/((2/self.position_magnitude)-((self.velocity_magnitude*\
                                self.velocity_magnitude)/self.gravitational_constant))
        self.orbital_elements_values_dict["SemiMajorAxis"] = self.semi_major_axis
    
    def calculate_inclination(self):
        self.inclination = (np.arccos((np.dot(self.angular_momentum_vector, self.K))/\
                            np.linalg.norm(self.angular_momentum_vector)))
        self.orbital_elements_values_dict["Inclination"] = self.inclination
        
    def adjust_angle(reference_value, angle):
        if reference_value >= 0:
            return angle
        else:
            return 2*np.pi - angle
    
    def calculate_argument_of_periapsis(self):
        self.argument_of_perigee = np.arccos(np.dot(self.n_vector, self.eccentricity_vector)/\
                                            (self.n_vector_magnitude*self.eccentricity))
        self.argument_of_perigee = OrbitalElements.adjust_angle(self.eccentricity_vector[2], self.argument_of_perigee)    
        self.orbital_elements_values_dict["ArgumentOfPerigee"] = self.argument_of_perigee
        
    def calculate_RAAN(self):
        self.RAAN = np.arccos(self.n_vector[0]/ 
                              self.n_vector_magnitude)
        self.RAAN = OrbitalElements.adjust_angle(self.n_vector[1], self.RAAN)
        self.orbital_elements_values_dict["RightAscensionofAscendingNode"] = self.RAAN
            
    def calculate_true_anomaly(self):
        self.true_anomaly = np.arccos((np.dot(self.eccentricity_vector,self.position_vector))/\
                            (self.eccentricity*self.position_magnitude))
        self.true_anomaly = OrbitalElements.adjust_angle(self.radial_velocity, self.true_anomaly)
        self.orbital_elements_values_dict["TrueAnomaly"] = self.true_anomaly
    
    # alternate orbital elements
    def calculate_argument_of_latitude(self):
        self.argument_of_latitude = np.arccos(np.dot(self.n_vector,self.position_vector)/\
                                    (self.position_magnitude*self.position_magnitude))
        self.argument_of_latitude = OrbitalElements.adjust_angle(self.eccentricity_vector[2], self.argument_of_latitude)
        self.orbital_elements_values_dict["ArgumentOfLatitude"] = self.argument_of_latitude
        
    def calculate_true_longitude(self):
        self.true_longitude = np.arccos(np.dot(self.I, self.position_vector)/self.position_magnitude)
        self.true_longitude = OrbitalElements.adjust_angle(self.radial_velocity, self.true_longitude)
        self.orbital_elements_values_dict["TrueLongitude"] = self.true_longitude
    
    def calculate_longitude_of_periapsis(self):
        self.longitude_of_perigee = np.arccos(np.dot(self.eccentricity_vector, self.I)/self.eccentricity)
        self.orbital_elements_values_dict["LongitudeOfPerigee"] = self.longitude_of_perigee
        
        
    def calculate(self):
        OrbitalElements.calculate_angular_momentum(self)
        OrbitalElements.calculate_eccentricity(self)
        OrbitalElements.calculate_semi_major_axis(self)
        OrbitalElements.calculate_node_line_vector(self)
        OrbitalElements.calculate_inclination(self)
        OrbitalElements.direction_of_the_satellite(self)
        if self.inclination != 0 or np.pi and self.eccentricity > 0:
            OrbitalElements.calculate_RAAN(self)
            OrbitalElements.calculate_argument_of_periapsis(self)
            OrbitalElements.calculate_true_anomaly(self)
        elif self.inclinaion == 0 or np.pi:
            if self.eccentricity > 0:
                OrbitalElements.calculate_longitude_of_periapsis(self)
                OrbitalElements.calculate_true_anomaly(self)
            else:
                OrbitalElements.calculate_true_longitude
        elif self.inclination != 0 or np.pi and self.eccentricity == 0:
            OrbitalElements.calculate_RAAN(self)
            OrbitalElements.calculate_argument_of_latitude(self)
        
        return self.orbital_elements_values_dict
            
    
    def locate_quadrant(self):
        if self.n_vector[0] > 0 and self.n_vector[1] > 0: 
            return "first quadrant"
        elif self.n_vector[0] < 0 and self.n_vector[1] > 0:
            return "seconnd quadrant"
        elif self.n_vector[0] < 0 and self.n_vector[1] < 0:
            return "third quadrant"
        elif self.n_vector[0] > 0 and self.n_vector[1] < 0:
            return "forth quadrant"
    
    def direction_of_orbit(self):
        if self.inclination < 90:
            return "prograde orbit"
        else:
            return "retrograde orbit"
    
    def direction_of_the_satellite(self):
        self.radial_velocity = np.dot(self.position_vector, self.velocity_vector)/self.radius_of_orbit
        if self.radial_velocity >= 0:
            self.satellite_direction = 'away from periapsis'
        else:
            self.satellite_direction = 'towards periapsis'
            
    def position_of_n_vector(self):
        self.RAAN_quadrant = OrbitalElements.locate_quadrant()
        self.orbit_direction = OrbitalElements.direction_of_orbit()
        
        if self.position_vector[0] == 0 and self.position_vector[1] == 0:
            self.n_vector_location_message = "The n vector cannot be defined as there is no Orbital Inclination"
        else:
            self.n_vector_location_message = f'This is a {self.orbit_direction} and Right Ascension of \
                                                Ascending Node(RAAN) lies in {self.RAAN_quadrant}'


if __name__ == '__main__':
    import pandas as pd
    
    position_vector = [8250, 390, 6900]
    velocity_vector = [-0.7, 6.6, -0.6]
    test1 = OrbitalElements('Earth',position_vector=position_vector, velocity_vector=velocity_vector)
    orbital_elements = test1.calculate()
    print(orbital_elements)
    # orbital_elements_df = pd.DataFrame.from_dict(orbital_elements)
    # pd.set_option('display.max_columns', None)
    # print(orbital_elements_df.T)
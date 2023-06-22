import numpy as np
import warnings
import constants.GlobalConstants as GCs
import constants.planetarydetails as pandet
from orbit import Orbit

class OrbitalElements():
    def __init__(self, *orbits):
        self.orbits = orbits
        # self.major_body_mass = pandet.value(major_body.lower(), 'mass')
        
        # self.position_vector = position_vector
        # self.velocity_vector = velocity_vector
        # self.orbital_elements_values_dict = {}
        
        # self.semi_major_axis = semi_major_axis
        # self.eccentricity = eccentricity
        # self.inclination = inclination
        # self.RAAN = RAAN
        # self.argument_of_periapsis = argument_of_periapsis
        # self.true_anomaly = true_anomaly
        
        self.G = GCs.NEWTON_GRAVITATIONAL_CONSTANT
        self.I = GCs.IVECTOR
        self.J = GCs.JVECTOR
        self.K = GCs.KVECTOR
        for orbit in orbits:
            orbit.MajorBodyMass = pandet.value(orbit.MajorBody, 'mass')
            orbit.gravitational_constant = GCs.NEWTON_GRAVITATIONAL_CONSTANT * orbit.MajorBodyMass
    
    
    # these are independent of the rest of class #TODO Seperate these into their own file
    def angle_between_two_vectors(self, vector_1, vector_2):
        vector_1_magnitude, vector_2_magnitude = self.get_magnitudes(vector_1, vector_2)
        return np.arccos(np.dot(vector_1, vector_2)/(vector_1_magnitude*vector_2_magnitude))
    
    def get_magnitudes(self, *vectors):
        return [np.linalg.norm(vector) for vector in vectors]
        
    # calculations for position vectors and velocity vectors to orbital elements
    def calculate_angular_momentum(self):
        for orbit in self.orbits:
            orbit.AngularMomentumVector = [np.cross(_position_vector, _velocity_vector) for _position_vector, _velocity_vector in zip(orbit.PositionVector, orbit.VelocityVector)]
            orbit.AngularMomentum = [np.linalg.norm(_angular_momentum_vector) for _angular_momentum_vector in orbit.AngularMomentumVector][0]
    
    def calculate_node_line_vector(self):
        for orbit in self.orbits:
            orbit.NodalVector = [np.cross(GCs.KVECTOR, _angular_momentum_vector) for _angular_momentum_vector in orbit.AngularMomentumVector]
            orbit.NVectorMagnitude = [np.linalg.norm(_n) for _n in orbit.NodalVector][0]
        # self.orbital_elements_names["NodalVector"] = self.n_vector
    
    def calculate_eccentricity(self):
        for orbit in self.orbits:
            orbit.EccentricityVector = [(np.multiply((vel**2-orbit.GravitationalConstant/pos),posvec)-np.multiply(np.dot(posvec, velvec), velvec))/orbit.GravitationalConstant \
                                        for mu, pos, vel, posvec, velvec in zip(orbit.PositionMagnitude, 
                                                                                orbit.VelocityMagnitude,
                                                                                orbit.PositionVector, 
                                                                                orbit.VelocityVector)]
            
            orbit.Eccentricity = [np.linalg.norm(eccvec) for eccvec in orbit.EccentricityVector][0]
    
    def calculate_semi_major_axis(self):
        for orbit in self.orbits:
            orbit.SemiMajorAxis = 1/((2/orbit.PositionMagnitude[0])-((orbit.VelocityMagnitude[0]*\
                                    orbit.VelocityMagnitude[0])/orbit.GravitationalConstant))
    
    def calculate_inclination(self):
        for orbit in self.orbits:
            orbit.Inclination = [np.arccos((np.dot(angular_momentum_vector, GCs.KVECTOR))/\
                                    np.linalg.norm(angular_momentum_vector)) for angular_momentum_vector in orbit.AngularMomentumVector][0]
        
    def adjust_angle(reference_value, angle):
        if reference_value >= 0:
            return angle
        else:
            return 2*np.pi - angle
    
    def calculate_argument_of_periapsis(self):
        for orbit in self.orbits:
            _argument_of_periapsis = (np.arccos(np.dot(orbit.NodalVector[0], orbit.EccentricityVector[0])/\
                                                (orbit.NVectorMagnitude*orbit.Eccentricity)))
            orbit.ArgumentOfPeriapsis = OrbitalElements.adjust_angle(orbit.EccentricityVector[0][2], _argument_of_periapsis)
        
    def calculate_RAAN(self):
        for orbit in self.orbits:
            _RAAN = np.arccos(orbit.NodalVector[0][0]/ 
                                orbit.NVectorMagnitude)
            orbit.RightAscensionOfAscendingNode = OrbitalElements.adjust_angle(self.n_vector[1], _RAAN)
            
            
    def calculate_true_anomaly(self):
        for orbit in self.orbits:
            _true_anomaly = [np.arccos((np.dot(eccentricity_vector, position_vector))/(orbit.Eccentricity*position_magnitude)) 
                             for eccentricity_vector, position_vector, position_magnitude in zip(orbit.EccentricityVector, 
                                                                                                 orbit.PositionVector, 
                                                                                                 orbit.PositionMagnitude)]
            orbit.TrueAnomaly = [OrbitalElements.adjust_angle(orbit.RadialVelocity, _true_anomaly)]
    
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
        for orbit in self.orbits:
            orbit.RadialVelocity = np.dot(orbit.PositionVector[0], orbit.VelocityVector[0])/orbit.position_magnitude[0]
            orbit.RadialVelocity = [np.dot(posvec, velvec)/pos for pos, posvec, velvec in zip(orbit.PositionVector,
                                                                                            orbit.VelocityVector,
                                                                                            orbit.PositionMagnitude)]
            if orbit.RadialVelocity[0] >= 0:
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
                                                
    def calculate(self, type):
        if type == 'get_orbital_elements':
            self.position_magnitude, self.velocity_magnitude = self.radius_of_orbit, self.velocity = \
            self.get_magnitudes(self.position_vector, self.velocity_vector)
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
        
        elif type == 'get_state_vectors':
            pass
        
    def get_orbital_values(self):
        try:
            if self.position_vector and self.velocity_vector != None:
                return OrbitalElements.calculate(self, 'get_orbital_elements')
            else:
                a = 1/0
        except:
            warnings.warn("Wrong pairs of values entered. Please check again.")
    



if __name__ == '__main__':
    
    orbit_1 = Orbit(MajorBody='Earth', PositionVector=[(8250, 390, 6900)], VelocityVector=[(-0.7, 6.6, -0.6)])
    position_vector = [8250, 390, 6900]
    velocity_vector = [-0.7, 6.6, -0.6]

    test1 = OrbitalElements('Earth',position_vector=position_vector, velocity_vector=velocity_vector)
    orbital_elements = test1.get_orbital_values()
    print(orbital_elements)
    # orbital_elements_df = pd.DataFrame.from_dict(orbital_elements)
    # pd.set_option('display.max_columns', None)
    # print(orbital_elements_df.T)
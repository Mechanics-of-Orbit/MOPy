# considdering renaming OrbitalManeuvers

import numpy as np
import constants.planetarydetails as pandet
import constants.GlobalConstants as GCs
from orbitalparameters import OrbitalValues

class HohmannTransfer():
    """
    
    ### !!! Enter any of the two values' pairs only to avoid over constrained situation!!! 
    ### !!! like ra,ecc or ecc, sma or sma, ecc
    
    
    Variables Definition:
    initial_orbit = {'radius_of_perigee': 10000, 'radius_of_apogee': 20000}
    final_orbit = {'eccentricity': 0.4, 'semi_major_axis': 15000}
    
    
    """
    def __init__(self, major_body, initial_orbit, final_orbit):
        self.major_body = major_body
        self.major_body_mass = pandet.value(major_body, 'mass')
        self.initial_orbit = initial_orbit
        self.final_orbit = final_orbit
        HohmannTransfer.extract_values_from_dict(self)
        HohmannTransfer.calculate_velocities(self)

    
    def calculate_deltav(self, cases=1):
        #transfer_1
        self.delta_velocity_transfer_1_initial_fire = self.transfer_1_velocity_at_perigee - self.initial_velocity_at_perigee
        self.delta_velocity_transfer_1_final_fire = self.transfer_1_velocity_at_apogee - self.final_velocity_at_apogee
        self.total_delta_velocity_transfer_1 = abs(self.delta_velocity_transfer_1_initial_fire) + abs(self.delta_velocity_transfer_1_final_fire)
        #transfer_2
        self.delta_velocity_transfer_2_initial_fire = self.transfer_2_velocity_at_perigee - self.initial_velocity_at_apogee
        self.delta_velocity_transfer_2_final_fire = self.transfer_2_velocity_at_apogee - self.final_velocity_at_perigee
        self.total_delta_velocity_transfer_2 = abs(self.delta_velocity_transfer_2_initial_fire) + abs(self.delta_velocity_transfer_2_final_fire)
        
        if cases == 1:
            return self.delta_velocity_transfer_1_initial_fire, self.delta_velocity_transfer_1_final_fire, self.total_delta_velocity_transfer_1
        elif cases == 2:
            return [self.delta_velocity_transfer_1_initial_fire, self.delta_velocity_transfer_1_final_fire, self.total_delta_velocity_transfer_1], \
                    [self.delta_velocity_transfer_2_initial_fire, self.delta_velocity_transfer_2_final_fire, self.total_delta_velocity_transfer_2]
        
    
    def calculate_velocities(self):
        initial_orbit_velocities = self.initial_orbit_values.calculate_velocities_at_these_points(self.initial_radius_of_apogee,
                                                                                    self.initial_radius_of_perigee)
        final_orbit_velocities = self.final_orbit_values.calculate_velocities_at_these_points(self.final_radius_of_apogee,
                                                                                    self.final_radius_of_perigee)
        
        transfer_1_velocities = self.transfer_1_orbit_values.calculate_velocities_at_these_points(self.transfer_1_radius_of_apogee,
                                                                                    self.transfer_1_radius_of_perigee)
        transfer_2_velocities = self.transfer_2_orbit_values.calculate_velocities_at_these_points(self.transfer_2_radius_of_apogee,
                                                                                    self.transfer_2_radius_of_perigee)
        
        self.initial_velocity_at_apogee = initial_orbit_velocities[0]
        self.initial_velocity_at_perigee = initial_orbit_velocities[1]
        self.final_velocity_at_apogee = final_orbit_velocities[0]
        self.final_velocity_at_perigee = final_orbit_velocities[1]
        self.transfer_1_velocity_at_apogee = transfer_1_velocities[0]
        self.transfer_1_velocity_at_perigee = transfer_1_velocities[1]
        self.transfer_2_velocity_at_apogee = transfer_2_velocities[0]
        self.transfer_2_velocity_at_perigee = transfer_2_velocities[1]
    
    def extract_values_from_dict(self):
        self.initial_semi_major_axis = self.initial_eccentricity = self.initial_radius_of_perigee = self.initial_radius_of_apogee = None
        self.final_semi_major_axis = self.final_eccentricity = self.final_radius_of_perigee = self.final_radius_of_apogee = None
        # for orbit_1
        for key, value in self.initial_orbit.items():
            if key == 'semi_major_axis':
                self.initial_semi_major_axis = value
            elif key == 'eccentricity':
                self.initial_eccentricity = value
            elif key == 'radius_of_perigee':
                self.initial_radius_of_perigee = value
            elif key == 'radius_of_apogee':
                self.initial_radius_of_apogee = value
            else:
                self.warning = "wrong keyword entered"
        
        
        for key, value in self.final_orbit.items():
            if key == 'semi_major_axis':
                self.final_semi_major_axis = value
            elif key == 'eccentricity':
                self.final_eccentricity = value
            elif key == 'radius_of_perigee':
                self.final_radius_of_perigee = value
            elif key == 'radius_of_apogee':
                self.final_radius_of_apogee = value
            else:
                self.warning = "wrong keyword entered"
        
        self.initial_orbit_values = OrbitalValues(self.major_body,
                                            semi_major_axis = self.initial_semi_major_axis, 
                                            eccentricity = self.initial_eccentricity, 
                                            radius_of_perigee = self.initial_radius_of_perigee, 
                                            radius_of_apogee = self.initial_radius_of_apogee)
        self.final_orbit_values = OrbitalValues(self.major_body,
                                            semi_major_axis = self.final_semi_major_axis, 
                                            eccentricity = self.final_eccentricity, 
                                            radius_of_perigee = self.final_radius_of_perigee, 
                                            radius_of_apogee = self.final_radius_of_apogee)
        
        self.initial_orbit_dict = self.initial_orbit_values.caculate_orbital_values()
        self.final_orbit_dict = self.final_orbit_values.caculate_orbital_values()
        
        
        self.initial_semi_major_axis = self.initial_orbit_dict['SemiMajorAxis']
        self.initial_eccentricity = self.initial_orbit_dict['Eccentricity']
        self.initial_radius_of_perigee = self.initial_orbit_dict['RadiusOfPerigee']
        self.initial_radius_of_apogee = self.initial_orbit_dict['RadiusOfApogee']
        
        self.final_semi_major_axis = self.final_orbit_dict['SemiMajorAxis']
        self.final_eccentricity = self.final_orbit_dict['Eccentricity']
        self.final_radius_of_perigee = self.final_orbit_dict['RadiusOfPerigee']
        self.final_radius_of_apogee = self.final_orbit_dict['RadiusOfApogee']
        
        #transfer orbit 1 --> initial orbit perigee to final orbit apogee
        self.transfer_1_radius_of_perigee = self.initial_radius_of_perigee
        self.transfer_1_radius_of_apogee = self.final_radius_of_apogee
        
        self.transfer_1_orbit_values = OrbitalValues(self.major_body,
                                            radius_of_perigee = self.transfer_1_radius_of_perigee, 
                                            radius_of_apogee = self.transfer_1_radius_of_apogee)
        self.transfer_1_orbit_dict = self.transfer_1_orbit_values.caculate_orbital_values()
        
        self.transfer_1_semi_major_axis = self.transfer_1_orbit_dict['SemiMajorAxis']
        self.transfer_1_eccentricity = self.transfer_1_orbit_dict['Eccentricity']
        self.transfer_1_radius_of_perigee = self.transfer_1_orbit_dict['RadiusOfPerigee']
        self.transfer_1_radius_of_apogee = self.transfer_1_orbit_dict['RadiusOfApogee']
        
        #transfer orbit 1 --> initial orbit apogee to final orbit perigee
        self.transfer_2_radius_of_perigee = self.initial_radius_of_apogee
        self.transfer_2_radius_of_apogee = self.final_radius_of_perigee
        
        self.transfer_2_orbit_values = OrbitalValues(self.major_body,
                                            radius_of_perigee = self.transfer_2_radius_of_perigee, 
                                            radius_of_apogee = self.transfer_2_radius_of_apogee)
        self.transfer_2_orbit_dict = self.transfer_2_orbit_values.caculate_orbital_values()
        
        self.transfer_2_semi_major_axis = self.transfer_2_orbit_dict['SemiMajorAxis']
        self.transfer_2_eccentricity = self.transfer_2_orbit_dict['Eccentricity']
        self.transfer_2_radius_of_perigee = self.transfer_2_orbit_dict['RadiusOfPerigee']
        self.transfer_2_radius_of_apogee = self.transfer_2_orbit_dict['RadiusOfApogee']

        

if __name__ == '__main__':
    initial_orbit = {'radius_of_perigee': 10000, 'radius_of_apogee': 20000}
    final_orbit = {'eccentricity': 0.4, 'semi_major_axis': 15000}
    
    transfer_1 = HohmannTransfer('Earth', initial_orbit, final_orbit)
    print(transfer_1.calculate_deltav(2))
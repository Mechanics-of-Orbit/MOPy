import numpy as np
import matplotlib.pyplot as plt
from orbitalparameters import OrbitalValues
import constants.planetarydetails as pandet
import constants.GlobalConstants as GCs


class plotter():
    def __init__(self, major_body,
                radius_of_apogee=None, 
                radius_of_perigee=None, 
                semi_major_axis=None, 
                eccentricity=None,
                start_end_angle=[0, 2*np.pi],
                orbit_resolution=1000):
        self.major_body = major_body
        self.major_body_mass = pandet.value(major_body, 'mass')
        self.gravitational_constant = GCs.NEWTON_GRAVITATIONAL_CONSTANT * self.major_body_mass
        self.radius_of_apogee = radius_of_apogee
        self.radius_of_perigee = radius_of_perigee
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        self.orbital_values = OrbitalValues(self.major_body, self.radius_of_apogee, 
                                        self.radius_of_perigee,
                                        self.semi_major_axis,
                                        self.eccentricity)
        self.orbital_values_dict = self.orbital_values.caculate_orbital_values()
        self.start_angle, self.end_angle = start_end_angle[0], start_end_angle[1]
        self.orbit_resolution = orbit_resolution

    def get_orbit_plot_points(self):
        theta = np.linspace(self.start_angle, self.end_angle, self.orbit_resolution)
        radii_points=(self.orbital_values_dict['SpecificAngularMomentum']**2/\
                    self.gravitational_constant)/(1+self.orbital_values_dict['Eccentricity']*np.cos(theta))
        self.x_coordinates = radii_points*np.sin(theta)
        self.y_coordinates = radii_points*np.cos(theta)

    def plot_orbit(self, show_body=True,show_orbit=True, **kwargs):
        plotter.get_orbit_plot_points(self)
        theta_body = np.linspace(0, 2*-np.pi, self.orbit_resolution)
        theta_orbit = np.linspace(self.start_angle, self.end_angle, self.orbit_resolution)
        
        radius_of_body = pandet.value(self.major_body,'diameter')/2
        self.major_body_color = pandet.value(self.major_body, 'color')
        plt.plot(self.x_coordinates, self.y_coordinates, **kwargs)

        if show_body:
            plt.fill(radius_of_body*np.sin(theta_body), radius_of_body*np.cos(theta_body), self.major_body_color)
            ax = plt.gca()
            ax.set_facecolor((0.0, 0.0, 0.0))
            ax.set_aspect('equal', adjustable='box')
            plt.show()
        # if show_orbit:
        #         plt.show()
    
        

if __name__ == '__main__':
    orbit_values = plotter('Earth', radius_of_apogee=25000, eccentricity=0.3, start_end_angle=[0, np.pi/2])
    orbit_values.plot_orbit(show_orbit=False, color='red')
    orbit_values_2 = plotter('Earth', radius_of_apogee=25000, eccentricity=0.4, start_end_angle=[0, np.pi])
    orbit_values_2.plot_orbit(show_orbit=False, color='blue')
import numpy as np
import matplotlib.pyplot as plt
from orbitalparameters import OrbitalValues
import constants.planetarydetails as pandet
import constants.GlobalConstants as GCs


class Plotter:
    """
    orbitss = {'orbit_1': {
                'radius_of_apogee': 125, 'radius_of_perigee': 00000, 
                'semi_major_axis': 00000, 'eccentricity': 00000, 
                'start_end_angle':[0, 2], 'orbit_resolution':1000
                  }
               }
    """
    def __init__(self, orbit_ax, major_body,
                 radius_of_apogee=None,
                 radius_of_perigee=None,
                 semi_major_axis=None,
                 eccentricity=None,
                 start_end_angle=None,
                 orbit_resolution=1000,
                 **entered_orbits):
        if start_end_angle is None:
            start_end_angle = [0, 2 * np.pi]
        self.major_body_color = None
        self.y_coordinates = None
        self.x_coordinates = None
        self.ax = orbit_ax
        self.major_body = major_body
        self.major_body_mass = pandet.value(major_body, 'mass')
        self.gravitational_constant = GCs.NEWTON_GRAVITATIONAL_CONSTANT * self.major_body_mass
        self.plot_details = {} # {'orbit_0' : {'start_angle': 00, 'end_angle': 11, 'orbit_resolution': 0000}, ....}
        self.all_orbits, self.orbit_name = Plotter.divide_the_orbits(**entered_orbits)
        self.all_orbital_values = {}
        for orbit_no, orbit in self.all_orbits.items():
            self.plot_details[orbit_no] = {'start_angle': orbit.get('start_angle', 0), 'end_angle': orbit.get('end_angle', (2*np.pi)), 'orbit_resolution': orbit.get('orbit_resolution', 1000)}
            orbital_values = OrbitalValues(self.major_body, orbit.get('radius_of_apogee', None),
                                                 orbit.get('radius_of_perigee', None), orbit.get('semi_major_axis', None),
                                                 orbit.get('eccentricity', None))
            self.all_orbital_values[orbit_no] = orbital_values.calculate_orbital_values()
        
        
        self.radius_of_apogee = radius_of_apogee
        self.radius_of_perigee = radius_of_perigee
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        self.orbital_values = OrbitalValues(self.major_body, self.radius_of_apogee,
                                            self.radius_of_perigee,
                                            self.semi_major_axis,
                                            self.eccentricity)
        self.orbital_values_dict = self.orbital_values.calculate_orbital_values()
        self.start_angle, self.end_angle = start_end_angle[0], start_end_angle[1]
        self.orbit_resolution = orbit_resolution

    def divide_the_orbits(**group_orbits):
        all_orbits = {}
        orbit_name = {}
        for i,orbit in enumerate(group_orbits.items()):
            all_orbits[f'orbit_{i}'] = orbit[1]
            orbit_name[f'orbit_{i}'] = orbit[0]

        # for orbit_no, orbit in all_orbits.items():
        #     try:
        #         check_value = orbit['start_end_angle']

            # if orbit.get('start')
        
        return all_orbits, orbit_name

    def get_orbit_plot_points(self, orbit_no):
        _this_orbit_plot_details = self.plot_details.get(orbit_no)
        _this_orbit_plot_values = self.all_orbital_values.get(orbit_no)
        theta = np.linspace(_this_orbit_plot_details.get('start_angle'), _this_orbit_plot_details.get('end_angle'), _this_orbit_plot_details.get('orbit_resolution'))
        radii_points = (_this_orbit_plot_values.get('SpecificAngularMomentum') ** 2 /
                        self.gravitational_constant) / (1 + _this_orbit_plot_values.get('Eccentricity') * np.cos(theta))
        x_coordinates = radii_points * np.sin(theta)
        y_coordinates = radii_points * np.cos(theta)
        return x_coordinates, y_coordinates

    def plot_orbit(self, show_body=True, show_orbit=True, show_plot=True, **kwargs):
        
        radius_of_body = pandet.value(self.major_body, 'diameter') / 2
        theta_body = np.linspace(0, 2 * -np.pi, 1000)
        self.major_body_color = pandet.value(self.major_body, 'color')
        
        if show_body:
            self.ax.fill(radius_of_body * np.sin(theta_body), radius_of_body * np.cos(theta_body),
                         self.major_body_color)
            
        
        for orbit_no, orbit in self.all_orbital_values.items():
            _x, _y = self.get_orbit_plot_points(orbit_no)
            if show_orbit:
                ax.plot(_x, _y, **kwargs)
            
        
        if show_plot:
            self.ax.set_facecolor((0.0, 0.0, 0.0))
            self.ax.set_aspect('equal', adjustable='box')
            plt.show()


if __name__ == '__main__':
    orbitss = {'orbit_1': {
                    'radius_of_apogee': 12000, 'radius_of_perigee': 20000, 
                    'semi_major_axis': None, 'eccentricity': None, 
                    'start_angle':0, 'end_angle': 2, 'orbit_resolution':1000
                    },
            'orbit_2': {
                    'radius_of_apogee': 15000, 'radius_of_perigee': 7000                
                    }
            }
    
    fig, ax = plt.subplots(1)
    orbit_values = Plotter(ax, 'Earth', radius_of_apogee=25000, eccentricity=0.3, start_end_angle=[0, np.pi / 2], **orbitss)
    orbit_values.plot_orbit(show_plot=True, color='red')
    orbit_values_2 = Plotter(ax, 'Earth', radius_of_apogee=20000, eccentricity=0.4, start_end_angle=[0, np.pi])
    orbit_values_2.plot_orbit(show_plot=False, color='blue')

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
                'start_angle':0, 'end_angle': 2,
                'orbit_resolution':1000,s
                  }
               }
               
        can input the graph values in this if each plot needs different like color and plot style
    """

    def __init__(self, orbit_ax, major_body,
                 **entered_orbits):
        self.major_body_color = None
        self.y_coordinates = None
        self.x_coordinates = None
        self.ax = orbit_ax
        self.major_body = major_body
        self.major_body_mass = pandet.value(major_body, 'mass')
        self.gravitational_constant = GCs.NEWTON_GRAVITATIONAL_CONSTANT * self.major_body_mass
        self.plot_details = {}  # {'orbit_0' : {'start_angle': 00, 'end_angle': 11, 'orbit_resolution': 0000}, ....}
        self.all_orbits, self.orbit_name = self.rename_the_orbits(**entered_orbits)
        self.named_orbital_values = {}
        for orbit_no, orbit in self.all_orbits.items():
            self.plot_details[orbit_no] = {'start_angle': orbit.get('start_angle', 0),
                                           'end_angle': orbit.get('end_angle', (2 * np.pi)),
                                           'orbit_resolution': orbit.get('orbit_resolution', 1000),
                                           'orbit_color': orbit.get('orbit_color', 'red'),
                                           }
            orbital_values = OrbitalValues(self.major_body, orbit.get('radius_of_apogee', None),
                                           orbit.get('radius_of_perigee', None), orbit.get('semi_major_axis', None),
                                           orbit.get('eccentricity', None))
            self.named_orbital_values[orbit_no] = orbital_values.calculate_orbital_values()

    def rename_the_orbits(self, **group_orbits):
        all_orbits = {}
        orbit_name = {}
        for i, orbit in enumerate(group_orbits.items()):
            all_orbits[f'orbit_{i}'] = orbit[1]
            orbit_name[f'orbit_{i}'] = orbit[0]

        return all_orbits, orbit_name

    def get_orbit_plot_points(self, orbit_no):
        _this_orbit_plot_details = self.plot_details.get(orbit_no)
        _this_orbit_plot_values = self.named_orbital_values.get(orbit_no)
        theta = np.linspace(_this_orbit_plot_details.get('start_angle'), _this_orbit_plot_details.get('end_angle'),
                            _this_orbit_plot_details.get('orbit_resolution'))
        radii_points = (_this_orbit_plot_values.get('SpecificAngularMomentum') ** 2 /
                        self.gravitational_constant) / (1 + _this_orbit_plot_values.get('Eccentricity') * np.cos(theta))
        x_coordinates = radii_points * np.sin(theta)
        y_coordinates = radii_points * np.cos(theta)
        return x_coordinates, y_coordinates

    def plot_orbit(self, show_body=True, show_orbit=True, style='mopy', **kwargs):

        __all_x = []
        __all_y = []
        radius_of_body = pandet.value(self.major_body, 'diameter') / 2
        theta_body = np.linspace(0, 2 * -np.pi, 1000)
        self.major_body_color = pandet.value(self.major_body, 'color')

        if show_body:
            self.ax.fill(radius_of_body * np.sin(theta_body), radius_of_body * np.cos(theta_body),
                         self.major_body_color)

        for orbit_no, orbit in self.named_orbital_values.items():
            _x, _y = self.get_orbit_plot_points(orbit_no)
            _this_orbit_plot_details = self.plot_details.get(orbit_no)
            kwargs['color'] = _this_orbit_plot_details.get('orbit_color')
            # color = _this_orbit_plot_details.get('orbit_color')
            __all_x.append(_x)
            __all_y.append(_y)
            graphs_limits = 1
            if show_orbit:
                self.ax.plot(_x, _y, **kwargs)

        if style == 'mopy':
            img = plt.imread(r'mopylib\assets\stars.jpeg')
            self.ax.imshow(img, extent=[np.min(np.array(__all_x)) * 1.1, np.max(np.array(__all_x)) * 1.1,
                                np.min(np.array(__all_y)) * 1.1, np.max(np.array(__all_y)) * 1.1])
            self.ax.set_facecolor((0.0, 0.0, 0.0))
            self.ax.set_aspect('equal', adjustable='box')


        return plt, self.ax


if __name__ == '__main__':
    
    orbits = {'initial': {
        'radius_of_apogee': 15000, 'radius_of_perigee': 10000,
        # 'semi_major_axis': None, 'eccentricity': None,
        'orbit_color': 'orange',
        'start_angle':0, 'end_angle': np.pi *- 2, 'orbit_resolution':1000
    },              
        'transfer_1': {
            'radius_of_apogee': 30000, 'radius_of_perigee': 10000,
            'orbit_color': 'pink',
            'start_angle':0, 'end_angle': 3/2 * np.pi, 'orbit_resolution':1000    
        },
        
        'final': {
            'semi_major_axis': 35000, 'radius_of_perigee': 30000
        },
    }
    
    

    fig, ax = plt.subplots(1, figsize=(25, 25))
    orbit_values = Plotter(ax, 'Earth', **orbits)
    orbit_plt, orbit_ax = orbit_values.plot_orbit(show_body=True, style='mopy')
    orbit_plt.show()

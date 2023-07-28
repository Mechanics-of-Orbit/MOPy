import numpy as np
import matplotlib.pyplot as plt
from orbitalparameters import OrbitalValues
import constants.planetarydetails as pandet
import constants.GlobalConstants as GCs
from maths import minmax_of_all
from orbit import PlotOrbit

class Plotter:
    """
    orbits = {'orbit_1': {
                'radius_of_apogee': 125, 'radius_of_perigee': 00000, 
                'semi_major_axis': 00000, 'eccentricity': 00000, 
                'start_angle':0, 'end_angle': 2,
                'orbit_resolution':1000,s
                  }
               }
               
        can input the graph values in this if each plot needs different like color and plot style
    """
    # TODO fix the for loop thingy
    def __init__(self, orbit_ax, *orbits):
        self.ax = orbit_ax
        _orbit_value = OrbitalValues(*orbits)
        self.orbits = _orbit_value.calculate_orbital_values()

    def keep_track_of_min_max(self):
        minmax_of_all(self.old_x, self.new_x)
        
    def get_orbit_plot_points(self):
        for orbit in self.orbits:
            theta = np.linspace(orbit.start_angle, orbit.end_angle, orbit.orbit_resolution)
            radii_points = (orbit.SpecificAngularMomentum ** 2 /
                            orbit.GravitationalConstant) / (1 + orbit.Eccentricity * np.cos(theta))
            orbit.x_coordinates = radii_points * np.sin(theta)
            orbit.y_coordinates = radii_points * np.cos(theta)

    def plot_orbit(self, show_body=True, show_orbit=True, style='mopy', **kwargs):

        # __all_x = []
        # __all_y = []

        if show_body:
            radius_of_body = pandet.value(self.orbits[0].MajorBody, 'diameter') / 2
            theta_body = np.linspace(0, 2 * -np.pi, 1000)
            self.major_body_color = pandet.value(self.orbits[0].MajorBody, 'color')
            self.ax.fill(radius_of_body * np.sin(theta_body), radius_of_body * np.cos(theta_body),
                         self.major_body_color)

        for orbit in self.orbits:
            self.get_orbit_plot_points()
            _x, _y = orbit.x_coordinates, orbit.y_coordinates
            # kwargs['color'] = orbit.get('orbit_color')
            # color = orbit.get('orbit_color')
            # _min_x = self.keep_track_of_min_max(_x)
            # _min_y = self.keep_track_of_min_max(_y)
            # print(self.xy_min)
            __all_x = [x for x in _x]
            __all_y = [y for y in _y]
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
    
    
    orbit_1 = PlotOrbit(MajorBody='Earth', SemiMajorAxis=20000, Eccentricity=0.5)
    orbit_2 = PlotOrbit(MajorBody='Earth', RadiusOfApogee=30000, Eccentricity=0.2, end_angle=2 * np.pi)

    

    fig, ax = plt.subplots(1, figsize=(25, 25))
    orbit_values = Plotter(ax, orbit_1, orbit_2)
    orbit_plt, orbit_ax = orbit_values.plot_orbit(show_body=True, style='mopy')
    
    orbit_plt.show()

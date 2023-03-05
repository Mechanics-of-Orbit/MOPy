import numpy as np
import constants.GlobalConstants as GCs
import constants.planetarydetails as pandet


class OrbitalValues:
    """The initiate the variables and calculate all the rest of the values related to the orbit based on the input.
    This take the given inputs and evaluates if the given information is enough to calculate the all the required
    orbital values. If not, it will return an error.
    
    ### !!! Enter any of the two values only to avoid over constrained situation!!!

    ------
    Example:
    >>> import mopylib.orbitalparameters as orbit_par
    >>> orbit_01 = orbit_par.OrbitalValues("Earth", semi_major_axis=20000, eccentricity=0.4)
    >>> orbit_01_values = orbit_1.calculate_orbital_values()
    >>> print(orbit_01_values)
    
    Output:
    >>> {'SemiMajorAxis': 20000, 'Eccentricity': 0.4, 'RadiusOfPerigee': 12000.0,
    'RadiusOfApogee': 28000.0, 'MeanMotion': 4480.043512802378, 'TimePeriod': 28148.943575165125, 
    'SpecificAngularMomentum': 81830.91404108841, 'SpecificMechanicalEnergy': -9.9647299, 'SemiLatusRectum': 16800.0}`
    
    ------
    Args:
        major_body (String): Name of the Major Body of the Orbit
        radius_of_apogee (float, optional): Radius of Apogee of the Orbit. Defaults to None.
        radius_of_perigee (float, optional): Radius of Perigee of the Orbit. Defaults to None.
        semi_major_axis (float, optional): Semi Major Axis of the Orbit. Defaults to None.
        eccentricity (Float, optional): Eccentricity of the Orbit. Defaults to None.
    """

    def __init__(self, major_body,
                 radius_of_apogee=None,
                 radius_of_perigee=None,
                 semi_major_axis=None,
                 eccentricity=None):
        self.specific_mechanical_energy = None
        self.mean_motion = None
        self.orbital_time_period = None
        self.specific_angular_momentum = None
        self.semi_latus_rectum = None
        self.gravitational_constant = None
        self.major_body = major_body
        self.major_body_mass = pandet.value(major_body, 'mass')
        self.radius_of_apogee = radius_of_apogee
        self.radius_of_perigee = radius_of_perigee
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        self.calculate_rest()

    def calculate_orbital_constants(self):
        self.gravitational_constant = GCs.NEWTON_GRAVITATIONAL_CONSTANT * self.major_body_mass
        self.semi_latus_rectum = self.semi_major_axis * (1 - self.eccentricity ** 2)
        self.specific_angular_momentum = (self.radius_of_perigee * (
                    1 + self.eccentricity) * self.gravitational_constant) ** 0.5
        self.orbital_time_period = np.sqrt(((4 * np.pi ** 2) / self.gravitational_constant) * self.semi_major_axis ** 3)
        self.mean_motion = self.orbital_time_period / (2 * np.pi)
        self.specific_mechanical_energy = -self.gravitational_constant / (2 * self.semi_major_axis)
        return self.mean_motion, self.orbital_time_period, self.specific_angular_momentum, \
            self.specific_mechanical_energy, self.semi_latus_rectum

    def calculate_rest(self):
        if self.radius_of_apogee and self.radius_of_perigee is not None:
            self.semi_major_axis = (self.radius_of_perigee + self.radius_of_apogee) / 2
            self.eccentricity = (self.radius_of_apogee - self.radius_of_perigee) / \
                                (self.radius_of_apogee + self.radius_of_perigee)
        elif self.semi_major_axis and self.eccentricity is not None:
            self.radius_of_perigee = self.semi_major_axis * (1 - self.eccentricity)
            self.radius_of_apogee = self.semi_major_axis * (1 + self.eccentricity)

        elif self.semi_major_axis and self.radius_of_apogee is not None:
            self.radius_of_perigee = 2 * self.semi_major_axis - self.radius_of_apogee
            self.eccentricity = (self.radius_of_apogee - self.radius_of_perigee) / \
                                (self.radius_of_apogee + self.radius_of_perigee)
        elif self.semi_major_axis and self.radius_of_perigee is not None:
            self.radius_of_apogee = 2 * self.semi_major_axis - self.radius_of_perigee
            self.eccentricity = (self.radius_of_apogee - self.radius_of_perigee) / \
                                (self.radius_of_apogee + self.radius_of_perigee)
        elif self.eccentricity and self.radius_of_apogee is not None:
            self.radius_of_perigee = self.radius_of_apogee * ((1 - self.eccentricity) / (1 + self.eccentricity))
            self.semi_major_axis = (self.radius_of_perigee + self.radius_of_apogee) / 2
        elif self.eccentricity and self.radius_of_perigee is not None:
            self.radius_of_apogee = self.radius_of_perigee * ((1 + self.eccentricity) / (1 - self.eccentricity))
            self.semi_major_axis = (self.radius_of_perigee + self.radius_of_apogee) / 2

        self.calculate_orbital_constants()

    def calculate_orbital_values(self, return_style='dict'):
        # possible values dict(default), variables
        if return_style == 'dict':
            orbital_values = {
                "SemiMajorAxis": self.semi_major_axis, "Eccentricity": self.eccentricity,
                "RadiusOfPerigee": self.radius_of_perigee, "RadiusOfApogee": self.radius_of_apogee,
                "MeanMotion": self.mean_motion, "TimePeriod": self.orbital_time_period,
                "SpecificAngularMomentum": self.specific_angular_momentum,
                "SpecificMechanicalEnergy": self.specific_mechanical_energy,
                "SemiLatusRectum": self.semi_latus_rectum
            }
            return orbital_values

        elif return_style == 'variables':
            return self.semi_major_axis, self.eccentricity, self.radius_of_perigee, self.radius_of_apogee, \
                self.mean_motion, self.orbital_time_period, self.specific_angular_momentum, self.specific_mechanical_energy, \
                self.semi_latus_rectum

    def calculate_velocities_at_these_angles(self, *angles):
        velocities = []
        for angle in angles:
            velocities.append(OrbitalValues.calculate_velocity_at_point(self, angle=angle))
        return velocities

    def calculate_velocities_at_these_points(self, *radii):
        velocities = []
        for radius in radii:
            velocities.append(OrbitalValues.calculate_velocity_at_point(self, radius=radius))
        return velocities

    def calculate_velocity_at_point(self, radius=None, angle=None):
        if angle is not None:
            radius = ((self.specific_angular_momentum ** 2 / self.gravitational_constant) / (
                    1 + self.eccentricity * np.cos(angle)))

        velocity = np.sqrt(
            (2 * self.gravitational_constant / radius) - (self.gravitational_constant / self.semi_major_axis))

        return velocity


if __name__ == '__main__':
    import pandas as pd

    sma = np.linspace(7000, 100000, num=15)
    e = np.linspace(0, 1, num=15, endpoint=False)
    # test = OrbitalValues("Earth", radiusOfApogee = 20000, radiusOfPerigee = 10000)
    # orbit_1 = OrbitalValues("Earth", semi_major_axis=20000, eccentricity=0)
    # orbit_1 = OrbitalValues("Earth", semi_major_axis=20000, eccentricity=0.4)
    # orbit_2 = OrbitalValues("Earth", semi_major_axis=20000, radius_of_apogee=28000)
    # orbit_3 = OrbitalValues("Earth", semi_major_axis=20000, radius_of_perigee=12000)
    # orbit_4 = OrbitalValues("Earth", eccentricity=0.4, radius_of_apogee=28000)
    # orbit_5 = OrbitalValues("Earth", eccentricity=0.4, radius_of_perigee=12000)
    # orbit_6 = OrbitalValues("Earth", radius_of_perigee=12000, radius_of_apogee=28000)
    for i, j in zip(sma, e):
        orbit_1 = OrbitalValues("Earth", semi_major_axis=i, eccentricity=j)
        print(f'{orbit_1.calculate_orbital_values()} \n')

    # orbital_values = [
    #             orbit_1.calculate_orbital_values(),
    #             # orbit_2.calculate_orbital_values(),
    #             # orbit_3.calculate_orbital_values(),
    #             # orbit_4.calculate_orbital_values(),
    #             # orbit_5.calculate_orbital_values(),
    #             # orbit_6.calculate_orbital_values()
    #             ]

    # orbital_values = [orbit_1.calculate_orbital_values()]
    # orbital_values_df = pd.DataFrame.from_dict(orbital_values)
    # # pd.set_option('display.max_columns', None)
    # # orbital_values_df.head()    
    # print(orbital_values_df.T)
    # print(orbital_values[0])

    print(orbit_1.calculate_velocities_at_these_angles(0, np.pi / 2, np.pi))

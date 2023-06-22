# import sys

# sys.path.insert(0, '.\src\constants')

import numpy as np
from constants import GlobalConstants as GCs
from constants import planetarydetails as pandet
from orbit import Orbit, PlotOrbit

class OrbitalValues:
    """The initiate the variables and calculate all the rest of the values related to the orbit based on the input.
    This take the given inputs and evaluates if the given information is enough to calculate the all the required
    orbital values. If not, it will return an error.
    
    ### !!! Enter any of the two values only to avoid over constrained situation!!!

    ------
    Example:
    >>> from mopylib.orbitalparameters import OrbitalValues
    >>> orbit_1_values = Orbit(MajorBody='Earth', SemiMajorAxis=20000, Eccentricity=0.5)
    >>> orbit_1 = OrbitalValues(orbit_1_values, orbit_2_values)
    >>> values = orbit_1.calculate_orbital_values()
    >>> print(values)
    >>> orbit_01 = orbit_par.OrbitalValues("Earth", SemiMajorAxis=20000, Eccentricity=0.4)
    >>> orbit_01_values = orbit_1.calculate_orbital_values()
    >>> print(orbit_01_values)
    
    Output:
    >>> Orbit(MajorBody='Earth', MajorBodyMass=5.972e+24, GravitationalConstant=398589.196, 
        SemiMajorAxis=20000, Eccentricity=0.5, RadiusOfPerigee=10000.0, RadiusOfApogee=30000.0, 
        MeanMotion=4480.043512802378, TimePeriod=28148.943575165125, SpecificAngularMomentum=77322.94575350838, 
        SpecificMechanicalEnergy=-9.9647299, SemiLatusRectum=15000.0)
    
    ------
    Args:
        orbits(Orbit Dataclass): unpacketed list of orbits in the form of Orbit Dataclass
    """

    def __init__(self, orbit):
        self.orbit = orbit
        self.calculate_values_not_entered()

    def calculate_orbital_constants(self):
        self.orbit.MajorBodyMass = pandet.value(self.orbit.MajorBody, 'mass')
        self.orbit.GravitationalConstant = GCs.NEWTON_GRAVITATIONAL_CONSTANT * self.orbit.MajorBodyMass
        self.orbit.SemiLatusRectum = self.orbit.SemiMajorAxis * (1 - self.orbit.Eccentricity ** 2)
        self.orbit.SpecificAngularMomentum = (self.orbit.RadiusOfPerigee * (
                    1 + self.orbit.Eccentricity) * self.orbit.GravitationalConstant) ** 0.5
        self.orbit.TimePeriod = np.sqrt(((4 * np.pi ** 2) / self.orbit.GravitationalConstant) * self.orbit.SemiMajorAxis ** 3)
        self.orbit.MeanMotion = self.orbit.TimePeriod / (2 * np.pi)
        self.orbit.SpecificMechanicalEnergy = -self.orbit.GravitationalConstant / (2 * self.orbit.SemiMajorAxis)

    def calculate_values_not_entered(self):
        if self.orbit.RadiusOfApogee and self.orbit.RadiusOfPerigee is not None:
            self.orbit.SemiMajorAxis = (self.orbit.RadiusOfPerigee + self.orbit.RadiusOfApogee) / 2
            self.orbit.Eccentricity = (self.orbit.RadiusOfApogee - self.orbit.RadiusOfPerigee) / \
                                (self.orbit.RadiusOfApogee + self.orbit.RadiusOfPerigee)
        
        elif self.orbit.SemiMajorAxis and self.orbit.Eccentricity is not None:
            self.orbit.RadiusOfPerigee = self.orbit.SemiMajorAxis * (1 - self.orbit.Eccentricity)
            self.orbit.RadiusOfApogee = self.orbit.SemiMajorAxis * (1 + self.orbit.Eccentricity)

        elif self.orbit.SemiMajorAxis and self.orbit.RadiusOfApogee is not None:
            self.orbit.RadiusOfPerigee = 2 * self.orbit.SemiMajorAxis - self.orbit.RadiusOfApogee
            self.orbit.Eccentricity = (self.orbit.RadiusOfApogee - self.orbit.RadiusOfPerigee) / \
                                (self.orbit.RadiusOfApogee + self.orbit.RadiusOfPerigee)
        
        elif self.orbit.SemiMajorAxis and self.orbit.RadiusOfPerigee is not None:
            self.orbit.RadiusOfApogee = 2 * self.orbit.SemiMajorAxis - self.orbit.RadiusOfPerigee
            self.orbit.Eccentricity = (self.orbit.RadiusOfApogee - self.orbit.RadiusOfPerigee) / \
                                (self.orbit.RadiusOfApogee + self.orbit.RadiusOfPerigee)
        
        elif self.orbit.Eccentricity and self.orbit.RadiusOfApogee is not None:
            self.orbit.RadiusOfPerigee = self.orbit.RadiusOfApogee * ((1 - self.orbit.Eccentricity) / \
                                                                      (1 + self.orbit.Eccentricity))
            self.orbit.SemiMajorAxis = (self.orbit.RadiusOfPerigee + self.orbit.RadiusOfApogee) / 2
        
        elif self.orbit.Eccentricity and self.orbit.RadiusOfPerigee is not None:
            self.orbit.RadiusOfApogee = self.orbit.RadiusOfPerigee * ((1 + self.orbit.Eccentricity) / \
                                                                      (1 - self.orbit.Eccentricity))
            self.orbit.SemiMajorAxis = (self.orbit.RadiusOfPerigee + self.orbit.RadiusOfApogee) / 2
        
        else:
            return 0
            
        self.calculate_orbital_constants()

    def calculate_orbital_values(self):
        return self.orbit

    def calculate_velocities_at_these_angles(self, *angles):
        return [OrbitalValues.calculate_velocity_at_point(self, angle=angle) for angle in angles]

    def calculate_velocities_at_these_points(self, *radii):
        return [OrbitalValues.calculate_velocity_at_point(self, radius=radius) for radius in radii]

    def calculate_velocity_at_point(self, radius=None, angle=None):
        if angle is not None:
            radius = ((self.SpecificAngularMomentum ** 2 / self.GravitationalConstant) / (
                    1 + self.Eccentricity * np.cos(angle)))

        velocity = np.sqrt(
            (2 * self.GravitationalConstant / radius) - (self.GravitationalConstant / self.SemiMajorAxis)
            )

        return velocity


if __name__ == '__main__':

    orbit_1_values = Orbit(MajorBody='Earth', SemiMajorAxis=67000, Eccentricity=0.8)
    # orbit_1_values = Orbit(MajorBody='Earth', RadiusOfApogee=155000+6378, RadiusOfPerigee=9000+6378)
    # orbit_1_plot = PlotOrbit(MajorBody='Earth', SemiMajorAxis=20000, Eccentricity=0.5)
    # plot_orbit = PlotOrbit()
    orbit_1 = OrbitalValues(orbit_1_values)
    values = orbit_1.calculate_orbital_values()
    print(values)
    # print(values[0].TimePeriod/(3600*24))
    # print(values[0].RadiusOfApogee)
    # print(values[0].RadiusOfPerigee)
    
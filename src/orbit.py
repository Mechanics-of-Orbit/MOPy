from dataclasses import dataclass, fields
import sys

import numpy as np


@dataclass()
class Orbit:
    """
     dataclass for storing orbital parameters and values
    >>> orbit_1 = Orbit(MajorBody="Earth", SemiMajorAxis=67000, Eccentricity=0.8)
    >>> orbit_1

    
    Attributes:
    -----------
    MajorBody: str = None
        Name of the Major Body
    MajorBodyMass: float = None
        Mass of the Major Body
    GravitationalConstant: float = None
        Gravitational Constant of the Major Body
    SemiMajorAxis: float = None
        Semi Major Axis of the Orbit
    Eccentricity: float = None
        Eccentricity of the Orbit
    Inclination: float = None
        Inclination of the Orbit
    ArgumentOfPeriapsis: float = None
        Argument of Periapsis of the Orbit
    RightAscensionOfAscendingNode: float = None
        Right Ascension of Ascending Node of the Orbit
    TrueAnamoly: list = None
        True Anamoly of the Orbit
    RadiusOfPerigee: float = None
        Radius of Perigee of the Orbit
    RadiusOfApogee: float = None
        Radius of Apogee of the Orbit
    MeanMotion: float = None
        Mean Motion of the Orbit
    TimePeriod: float = None
        Time Period of the Orbit
    SpecificAngularMomentum: float = None
        Specific Angular Momentum of the Orbit
    SpecificMechanicalEnergy: float = None
        Specific Mechanical Energy of the Orbit
    SemiLatusRectum: float = None
        Semi Latus Rectum of the Orbit
    NVectorMagnitude: float = None
        N Vector Magnitude of the Orbit
    EccentricityVector: list = None
        Eccentricity Vector of the Orbit
    SpecificAngularMomentumVector: list = None
        Specific Angular Momentum Vector of the Orbit
    SpecificMechanicalEnergyVector: list = None
        Specific Mechanical Energy Vector of the Orbit
    Points: list = None
        Points of the Orbit
    NodalVector: list = None
        Nodal Vector of the Orbit's points
    PositionVector: list = None
        Position Vector of the Orbit's points
    PositionMagnitude: list = None
        Position Magnitude of the Orbit's points
    VelocityVector: list = None
        Velocity Vector of the Orbit's points
    VelocityMagnitude: list = None
        Velocity Magnitude of the Orbit's points
    RadialVelocity: list = None
        Radial Velocity of the Orbit's points
    Velocity: list = None
        Velocity of the Orbit's points
    """
    # body's details
    MajorBody: str = None
    MajorBodyMass: float = None
    GravitationalConstant: float = None
    
    # orbital parameters
    SemiMajorAxis: float = None
    Eccentricity: float = None
    Inclination: float = None
    ArgumentOfPeriapsis: float = None
    RightAscensionOfAscendingNode: float = None
    RAAN: float = RightAscensionOfAscendingNode #TODO try multiple names for same variable
    TrueAnamoly: list = None
    
    # orbital constants
    RadiusOfPerigee: float = None
    RadiusOfApogee: float = None
    MeanMotion: float = None
    TimePeriod: float = None
    SpecificAngularMomentum: float = None
    SpecificMechanicalEnergy: float = None
    SemiLatusRectum: float = None
    NVectorMagnitude: float = None
    
    #vectors
    EccentricityVector: list = None
    SpecificAngularMomentumVector: list = None
    SpecificMechanicalEnergyVector: list = None
    NodalVector: list = None
    
    # orbital points
    Points: list = None
    PositionVector: list = None
    PositionMagnitude: list = None
    VelocityVector: list = None
    VelocityMagnitude: list = None
    RadialVelocity: list = None
    Velocity: list = None

@dataclass
class PlotOrbit(Orbit):
    """
    PlotOrbit Values for plotting orbits

    Parameters
    ----------
    Orbit : Orbit Class
        Values from Orbit Class
    start_angle : float, optional
        Starting angle for orbit, by default 0
    end_angle : float, optional
        Ending angle for orbit, by default 2*np.pi
    orbit_resolution : float, optional
        Resolution of orbit, by default 1000
    x_coordinates : list, optional
        x coordinates of orbit, by default None
    y_coordinates : list, optional
        y coordinates of orbit, by default None
    """
    start_angle: float = 0
    end_angle: float = 2*np.pi
    orbit_resolution: float = 1000
    x_coordinates: list = None
    y_coordinates: list = None

def main():
    orbit_1 = PlotOrbit(SemiMajorAxis=20000, RightAscensionOfAscendingNode=20, start_angle=0)
    return orbit_1


if __name__ == '__main__':
    test = main()
    print(test)
    pass
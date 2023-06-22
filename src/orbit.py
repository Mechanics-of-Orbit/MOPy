from dataclasses import dataclass
import numpy as np

@dataclass()
class Orbit:
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
    print(test.start_angle)
    pass
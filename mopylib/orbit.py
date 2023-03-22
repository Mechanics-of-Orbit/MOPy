from dataclasses import dataclass

@dataclass()
class Orbit:
    MajorBody: str = None
    SemiMajorAxis: float = None
    Eccentricity: float = None
    RadiusOfPerigee: float = None
    RadiusOfApogee: float = None
    MeanMotion: float = None
    TimePeriod: float = None
    SpecificAngularMomentum: float = None
    SpecificMechanicalEnergy: float = None
    SemiLatusRectum: float = None


def main():
    orbit_1 = Orbit(SemiMajorAxis=20000)
    return orbit_1


if __name__ == '__main__':
    test = main()
    print(test.SemiMajorAxis)
    pass
import numpy as np


def DSPS(rVecSat, rVecSun, PlanetRadius):
    rSat = np.linalg.norm(rVecSat)
    rSun = np.linalg.norm(rVecSun)
    
    # Angle between Sun and satellite
    theta = np.rad2deg(np.arccos(np.dot(rVecSat, rVecSun)/(rSat*rSun)))
    
    # Angle between Satellite and tangent through the planet
    thetaSat = np.rad2deg(np.arccos(PlanetRadius/rSat))
    
    # Angle between Satellite and tangent through the Sun
    thetaSun = np.rad2deg(np.arccos(PlanetRadius/rSun))
    
    # Checking the LOS with Sun and Satellite
    if thetaSat + thetaSun <= theta:
        inShadow = "It is in Shadow"
    else:
        inShadow = "It is Lit"
    return inShadow

if __name__ == '__main__':
    PlanetRadius = 6378# manju call from db
    rVecSun = [-11747041, 139486985, 60472278]
    rVecSat = [2817.899, -14110.473, -7502.672]
    Check = DSPS(rVecSat, rVecSun, PlanetRadius)
    print(Check)
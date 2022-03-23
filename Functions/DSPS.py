import numpy as np
PlanetRadius = 6378# manju call from db
def DSPS(rVecSat, rVecSun, PlanetRadius):
    rSat = np.linalg.norm(rVecSat)
    rSun = np.linalg.norm(rVecSun)
    
    # Angle between Sun and satellite
    theta = np.rad2deg(np.arccos(np.dot(rVecSat, rVecSun)/(rSar*rSun)))
    
    # Angle between Satellite and tangent through the planet
    thetaSat = np.rad2deg(np.arccos(PlanetRadius/rSat))
    
    # Angle between Satellite and tangent through the Sun
    thetaSun = np.rad2deg(np.arccos(np.PlanetRadius/rSun))
    
    # Checking the LOS with Sun and Satellite
    if thetaSat + thetaSun <= theta:
    
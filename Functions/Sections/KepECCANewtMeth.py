import numpy as np

# E - esin(E) = M
def keplerECCA(ecc, MeAnom)
    error = 1e-90

    if M < np.pi:
        ECCA = MeAnom + ecc/2
    else:
        ECCA = MeAnom - ecc/2
    
    ratio = 1
    while abs(ratio) > error:
        ratio = (ECCA - ecc*np.sin(E) - MeAnom)/(1 - ecc*np.cos(ECCA))
        ECCA = ECCA - ratio
    return ECCA
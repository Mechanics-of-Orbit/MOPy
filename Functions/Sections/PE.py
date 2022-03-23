import numpy as np
from KepECCANewtMeth import keplerECCA

# LoPeri ¼ longitude of perihelion ( ¼ RA + w) (deg)
# ML ¼ mean longitude ( ¼ w_hat + M) (deg)
# MA ¼ mean anomaly (deg)
# ECCA ¼ eccentric anomaly (deg)


elements_0 = [sma_0, ecc_0, inc_0, RAAN_0, omega_0, nu_0]
rates = [smaDot, eccDot, incDot, RAANDot, omegaDot, nuDot]
MajorBodyDetails = "Manjunath Call from DB"
def PECalculation(JDN, elements_0, rates, MajorBodyDetails):
    T_0 = (JDN-2451545)/36525
    elements = elements_0 + T_0 * np.array(rates)
    deg = np.pi/360
    # Call mu from db
    mu = 1
    sma = elements[0]
    ecc = elements[1]
    h = sqrt(mu*sma*(1-ecc**2))
    inc = elements[3]
    RAAN = zeroTo360(elements[4])
    LoPeri = zeroTo360(elements[5])
    omega = zeroTo360(LoPeri - RAAN)
    MeLong = zeroTo360(elements[6])
    MeAnom = zeroTo360(MeLong-LoPeri)
    ECCA = keplerECCA(ecc, MeAnom*deg)
    nu = zeroTo360(2*np.arctan(sqrt((1 + ecc)/(1 - ecc))*np.tan(ECCA/2))/deg)
    ACOE = [sma, ecc, h, inc, RAAN, LoPeri, omega, MeLong, MeAnom, ECCA, nu]
    return ACOE


def zeroTo360(x):
    if x>= 360
        x = x - int(x/360)*360
        return x
    elif x < 0
        x = x - (int(x/360)-1)*360
        return x
    

    
    
    
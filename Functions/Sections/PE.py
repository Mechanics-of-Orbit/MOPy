import numpy as np
from KepECCANewtMeth import keplerECCA



print("testing")
# LoPeri ¼ longitude of perihelion ( ¼ RA + w) (deg)
# ML ¼ mean longitude ( ¼ w_hat + M) (deg)
# MA ¼ mean anomaly (deg)
# ECCA ¼ eccentric anomaly (deg)
 
def PECalculation(JDN, elements_0, rates, SunMass):
    T_0 = (JDN-2451545)/36525
    print(T_0)
    elements = elements_0 + T_0 * np.array(rates)
    print(elements)
    deg = np.pi/360
    # Call mu from db
    G = 6.67e-20
    mu = G * SunMass
    sma = elements[0]
    ecc = elements[1]
    h = np.sqrt(mu*sma*(1-ecc**2))
    inc = elements[2]
    RAAN = zeroTo360(elements[3])
    LoPeri = zeroTo360(elements[4])
    omega = zeroTo360(LoPeri - RAAN)
    MeLong = zeroTo360(elements[5])
    MeAnom = zeroTo360(MeLong-LoPeri)
    ECCA = keplerECCA(ecc, MeAnom*deg)
    nu = zeroTo360(2*np.arctan(np.sqrt((1 + ecc)/(1 - ecc))*np.tan(ECCA/2))/deg)
    ACOE = [sma, ecc, h, inc, RAAN, LoPeri, omega, MeLong, MeAnom, ECCA, nu]
    return ACOE


def zeroTo360(x):
    if x>= 360:
        x = x - int(x/360)*360
        return x
    elif x < 0:
        x = x - (int(x/360)-1)*360
        return x
    else:
        return x

if __name__ == '__main__':
    from DB.call_database import call
    print("Testing")
    sma_0 = call.planetary_ephimeris("Earth","aAU")[0]
    ecc_0 = call.planetary_ephimeris("Earth","e")[0]
    inc_0 = call.planetary_ephimeris("Earth","iDeg")[0]
    RAAN_0 = call.planetary_ephimeris("Earth","RAANDeg")[0]
    omega_0 = call.planetary_ephimeris("Earth","OmegaDeg")[0]
    nu_0 = call.planetary_ephimeris("Earth","nudeg")[0]
    smaDot = call.planetary_ephimeris("Earth","aDotAUCentury-1")[0]
    eccDot = call.planetary_ephimeris("Earth","eDotCentury-1")[0]
    incDot = call.planetary_ephimeris("Earth","iDotDegCentury-1")[0]
    RAANDot = call.planetary_ephimeris("Earth","RAANDotDegCentury-1")[0]
    omegaDot = call.planetary_ephimeris("Earth","OmegaDotDegCentury-1")[0]
    nuDot = call.planetary_ephimeris("Earth","nuDotDegCentury-1")[0]
    # SunMass = call.data("Sun", "mass")[0]
    # DistFrmSun = call.data("Earth", "dist_frm_sun")[0]
    SunMass = 1.9885e30

    elements_0 = [sma_0, ecc_0, inc_0, RAAN_0, omega_0, nu_0]
    print(elements_0)
    rates = [smaDot, eccDot, incDot, RAANDot, omegaDot, nuDot]
    print(rates)
    
    
    # print(elements_0)
    # print(rates)
    
    PECheckEarth = PECalculation(2452879, elements_0, rates, SunMass)
    print(PECheckEarth)
    
    
    
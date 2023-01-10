import numpy as np
from scipy.constants import convert_temperature
from .GlobalConstants import *
from .sivalues import *
# planetary ephemeris
# Property                              Sun             Mercury      Venus      Earth       Mars         Jupiter        Saturn      Uranus        Neptune        Pluto
# -------------------------------------
planets_values_text = """\
Mass                                    1.9885e30       3.3e23       4.87e24    5.972e24    6.42e23     1.898e27        5.68e26     8.68e25       1.02e26        1.46e22
Diameter                                1391400         4879         12104      12756       6792        142984          120536      51118         49528          2370        
"""

stars_values_text = """\
    
"""
# todo write methods to calculate timeperiod, periapsis and apoapsis at a given time andd default to that days time
# todo write that they can call any unit, but default will be the value in dict
    # "data": {
    #     "category": "",
    #     "name": "",
    #     "mass": {"value": 1, "units": ["kg"]},
    #     "diameter": {"value": 1, "units": ["km"]},
    #     "density": {"value": 1, "units": ["kg/m3", "kg m-3"]},
    #     "acceleration_due_to_gravity": {"value": 1, "units": ["m/s2", "m s-2"]},
    #     "escape_velocity_from_surface": {"value": 1, "units": ["km/s", "km s-1"]},
    #     "rotation_period": {"value": 1, "units": ["hours"]},
    #     "length_of_day": {"value": 1, "units": ["hours"]},
    #     "distance_from_major_body": {"value": 1, "units": ["km"]},
    #     "semimajoraxis_0": {"value": 1, "units": ["AU"]},
    #     "semimajoraxis_dot": {"value": 1, "units": ["AU/century", "AUcentury-1"]},
    #     "eccentricity_0": {"value": 0, "units": [None]},
    #     "eccentricity_dot": {"value": 0, "units": ["1/century", "century-1"]},
    #     "inclination_0": {"value": 0, "units": ["degrees"]},
    #     "inclination_dot": {"value": 0, "units": ["degrees/century", "degrees century-1"]},
    #     "RAAN_0": {"value": 0, "units": ["degrees"]},
    #     "RAAN_dot": {"value": 0, "units": ["degrees/century", "degrees century-1"]},
    #     "argument_of_perigee_0": {"value": 102.93768193, "units": ["degrees"]},
    #     "argument_of_perigee_dot": {"value": 0.32327364, "units": ["degrees/century", "degrees century-1"]},
    #     "true_anomaly_0": {"value": 100.4645457166, "units": ["degrees"]},
    #     "true_anomaly_dot": {"value": 35999.37244981, "units": ["degrees/century", "degrees century-1"]},
    # }

values_dict = {
    "sun": {
        "category": "star",
        "name": "The Sun",
        "mass": {"value": "1.9885e30", "units": ["kg"]},
        "diameter": {"value": "1391400", "units": ["km"]},
        "density": {"value": "1409", "units": ["kg/m3", "kg m-3"]},
        "acceleration_due_to_gravity": {"value": "274", "units": ["m/s2", "m s-2"]},
        "escape_velocity_from_surface": {"value": "617.6", "units": ["km/s", "km s-1"]},
        "rotation_period": {"value": "609.12", "units": ["hours"]},
        "length_of_day": {"value": 0, "units": [""]},
        "distance_from_major_body": {"value": 0, "units": [""]},
        "semimajoraxis_0": {"value": 0, "units": [""]},
        "semimajoraxis_dot": {"value": 0, "units": [""]},
        "eccentricity_0": {"value": 0, "units": [""]},
        "eccentricity_dot": {"value": 0, "units": [""]},
        "inclination_0": {"value": 0, "units": [""]},
        "inclination_dot": {"value": 0, "units": [""]},
        "RAAN_0": {"value": 0, "units": [""]},
        "RAAN_dot": {"value": 0, "units": [""]},
        "argument_of_perigee_0": {"value": 0, "units": [""]},
        "argument_of_perigee_dot": {"value": 0, "units": [""]},
        "true_anomaly_0": {"value": 0, "units": [""]},
        "true_anomaly_dot": {"value": 0, "units": [""]},
    },
    "earth": {
        "category": "planet",
        "name": "Earth",
        "mass": {"value": 5.972e24, "units": ["kg"]},
        "diameter": {"value": 12756, "units": ["km"]},
        "density": {"value": 5514, "units": ["kg/m3", "kg m-3"]},
        "acceleration_due_to_gravity": {"value": 9.81, "units": ["m/s2", "m s-2"]},
        "escape_velocity_from_surface": {"value": 11.12, "units": ["km/s", "km s-1"]},
        "rotation_period": {"value": 23.9345, "units": ["hours"]},
        "length_of_day": {"value": 24, "units": ["hours"]},
        "distance_from_major_body": {"value": 149600000, "units": ["km"]},
        "semimajoraxis_0": {"value": 1.00000261, "units": ["AU"]},
        "semimajoraxis_dot": {"value": 5.62e-06, "units": ["AU/century", "AUcentury-1"]},
        "eccentricity_0": {"value": 0.01671121, "units": [None]},
        "eccentricity_dot": {"value": -4.392e-5, "units": ["1/century", "century-1"]},
        "inclination_0": {"value": -1.531e-5, "units": ["degrees"]},
        "inclination_dot": {"value": -0.01294668, "units": ["degrees/century", "degrees century-1"]},
        "RAAN_0": {"value": 0, "units": ["degrees"]},
        "RAAN_dot": {"value": 0, "units": ["degrees/century", "degrees century-1"]},
        "argument_of_perigee_0": {"value": 102.93768193, "units": ["degrees"]},
        "argument_of_perigee_dot": {"value": 0.32327364, "units": ["degrees/century", "degrees century-1"]},
        "true_anomaly_0": {"value": 100.4645457166, "units": ["degrees"]},
        "true_anomaly_dot": {"value": 35999.37244981, "units": ["degrees/century", "degrees century-1"]},
    }
    }


def parse_body_data(body, value,return_units=False):
    bodies_values = values_dict.get(body)
    if return_units:
        return (bodies_values[value]['units'])
    else:
        return (bodies_values[value]['value'])    



def value(body, value, units='default'):
    if units == 'default':
        return parse_body_data(body, value, return_units=False)
    else:
        if units in parse_body_data(body, value, return_units=True):
            return parse_body_data(body, value, return_units=False)
            

def units(body, value):
    return parse_body_data(body, value, return_units=True)[0]
    

def convert_units(old_value: float, old_unit: str, new_unit: str) -> float:
    """
    Converts values from one unit to another. Ensure all the units are fundamental and are not derived. 
    
    No hyphens or spaces apart from signs and seperating different units.
    > Inputs are Case Sensitive. for example - Kilo is K, Mega is M and milli is m. 
    
    ## Exceptions
    1. micro is `u` as using `m` clashs with milli
    
    format:
    >>> `convert_units(12502, 'Kg s+2 m-3', 'g s+2 cm-3')`
    >>> `result`

    Args:
        old_value (float): _description_
        old_unit (str): _description_
        new_unit (str): _description_

    Returns:
        float: _description_
    """
    def split_unit(input_unit):
        units_in_input_unit = input_unit.split()
        solo_units = []
        for values in units_in_input_unit:
            if len(values.split('-')) > 1:
                solo_units.append([values.split('-')[0],float('-' + values.split('-')[1])])
            elif len(values.split('+')) > 1:
                solo_units.append([values.split('+')[0],float(values.split('+')[1])])
            else:
                solo_units.append([values, 1])    
        return solo_units
    solo_units_old = split_unit(old_unit)
    solo_units_new = split_unit(new_unit)
    units_calculation = []
    
    for unit in solo_units_old:
        """
        possible strings in this case for different units:
        
        length - m and SI prefixes(mm, cm, km, um), AU, lightyear, ly, millimeter, micrometer, nanometer, kilometer
        mass - g and SI prefixes(mg, kg, ug)
        time - s, seconds, min, year, years, hour, hours
        angle - radians, degrees, rad, deg
        SI Prefix = ['Y', 'Z', 'E', 'P', 'T', 'G', 'M', 'K', 'H', 'D', 'd', 'c', 'm', 'u', 'n', 'p', 'f', 'a', 'z']
        """
        if unit[0][0] in SIV.SI_PREFIX:
            if unit[1] > 0:
                units_calculation.append(SIV.SI_PREFIX_VALUES[unit[0][0]])
            elif unit[1] < 0:
                pass
                # units_calculation.append(1/(SIV.SI_PREFIX_VALUES[unit[0][0]]))
                
            print(units_calculation)
        
        if unit[0] in POSSIBLE_TIME_CONSTANTS:
            multiple = TIME_VALUES[unit[0]]
            


if __name__ == '__main__':
    print(value('earth', 'mass'))
    # convert_units(12502, 'Kg s+2 m-3', 'g s+2 cm-3')
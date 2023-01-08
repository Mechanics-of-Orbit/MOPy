import numpy as np

# Property                              Sun             Mercury      Venus      Earth       Mars         Jupiter        Saturn      Uranus        Neptune        Pluto
# -------------------------------------
planets_values_text = """\
Mass                                    1.9885e30       3.3e23       4.87e24    5.972e24    6.42e23     1.898e27        5.68e26     8.68e25       1.02e26        1.46e22
Diameter                                1391400         4879         12104      12756       6792        142984          120536      51118         49528          2370        
"""

stars_values_text = """\
    
"""
# todo write methods to calculate timeperiod, periapsis and apoapsis at a given time andd default to that days time
# todo write that they can call anyunit, but default will be the value in dict
    # "data": {
    #     "id": "star",
    #     "name": "sun",
    #     "mass": {"value": "1.9885e30", "units": "kg"},
    #     "diameter": {"value": "", "units": ""},
    #     "density": {"value": "", "units": ""},
    #     "acceleration_due_to_gravity": {"value": "", "units": ""},
    #     "escape_velocity_from_surface": {"value": "", "units": ""},
    #     "rotation_period": {"value": "", "units": ""},
    #     "length_of_day": {"value": "", "units": ""},
    #     "distance_from_major_body": {"value": "", "units": ""},
    #     "semimajoraxis_0": {"value": "", "units": ""},
    #     "semimajoraxis_dot": {"value": "", "units": ""},
    #     "eccentricity_0": {"value": "", "units": ""},
    #     "eccentricity_dot": {"value": "", "units": ""},
    #     "inclination_0": {"value": "", "units": ""},
    #     "inclination_dot": {"value": "", "units": ""},
    #     "RAAN_0": {"value": "", "units": ""},
    #     "RAAN_dot": {"value": "", "units": ""},
    #     "argument_of_perigee_0": {"value": "", "units": ""},
    #     "argument_of_perigee_dot": {"value": "", "units": ""},
    #     "true_anomaly_0": {"value": "", "units": ""},
    #     "true_anomaly_dot": {"value": "", "units": ""},
    # }

planets_values_dict = {
    "data": {
        "id": "star",
        "name": "sun",
        "mass": {"value": "1.9885e30", "units": "kg"},
        "diameter": {"value": "1391400", "units": "km"},
        "density": {"value": "1409", "units": "kg/m3"},
        "acceleration_due_to_gravity": {"value": "274", "units": "m/s2"},
        "escape_velocity_from_surface": {"value": "617.6", "units": "km/s"},
        "rotation_period": {"value": "609.12", "units": "hours"},
        "length_of_day": {"value": "", "units": ""},
        "distance_from_major_body": {"value": "", "units": ""},
        "semimajoraxis_0": {"value": "", "units": ""},
        "semimajoraxis_dot": {"value": "", "units": ""},
        "eccentricity_0": {"value": "", "units": ""},
        "eccentricity_dot": {"value": "", "units": ""},
        "inclination_0": {"value": "", "units": ""},
        "inclination_dot": {"value": "", "units": ""},
        "RAAN_0": {"value": "", "units": ""},
        "RAAN_dot": {"value": "", "units": ""},
        "argument_of_perigee_0": {"value": "", "units": ""},
        "argument_of_perigee_dot": {"value": "", "units": ""},
        "true_anomaly_0": {"value": "", "units": ""},
        "true_anomaly_dot": {"value": "", "units": ""},
    },
    "data": {
        "id": "planet",
        "name": "earth",
        "mass": {"value": "5.97e24", "units": "kg"},
        "diameter": {"value": "12756", "units": "km"},
        "density": {"value": "5514", "units": "kg/m3"},
        "acceleration_due_to_gravity": {"value": "9.81", "units": "m/s2"},
        "escape_velocity_from_surface": {"value": "11.12", "units": "m/2"},
        "rotation_period": {"value": "23.9345", "units": "hours"},
        "length_of_day": {"value": "24", "units": "hours"},
        "distance_from_major_body": {"value": "149600000", "units": "km"},
        "semimajoraxis_0": {"value": "1.00000261", "units": "AU"},
        "semimajoraxis_dot": {"value": "5.62e-06", "units": ""},
        "eccentricity_0": {"value": "", "units": ""},
        "eccentricity_dot": {"value": "", "units": ""},
        "inclination_0": {"value": "", "units": ""},
        "inclination_dot": {"value": "", "units": ""},
        "RAAN_0": {"value": "", "units": ""},
        "RAAN_dot": {"value": "", "units": ""},
        "argument_of_perigee_0": {"value": "", "units": ""},
        "argument_of_perigee_dot": {"value": "", "units": ""},
        "true_anomaly_0": {"value": "", "units": ""},
        "true_anomaly_dot": {"value": "", "units": ""},
    }
    }


# def parse
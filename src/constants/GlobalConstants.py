from scipy.constants import gravitational_constant, kilo, speed_of_light

MINUTE = 60.0
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
YEAR = 365 * DAY
JULIAN_YEAR = 365.25 * DAY
POSSIBLE_TIME_CONSTANTS = ['s', 'seconds', 'minute', 'hour', 'hours', 'day', 'days', 'years', 'year']


# time in seconds 
TIME_VALUES = {
    'minute': MINUTE,
    'hour': HOUR,
    'hours': HOUR,
    'day': DAY,
    'days': DAY,
    'years': JULIAN_YEAR,
    'year': JULIAN_YEAR,
    
    
}


IVECTOR = [1, 0, 0]
JVECTOR = [0, 1, 0]
KVECTOR = [0, 0, 1]
NEWTON_GRAVITATIONAL_CONSTANT = gravitational_constant * kilo**-3 #units are in km3 kg-1 s-2
SPEED_OF_LIGHT = speed_of_light
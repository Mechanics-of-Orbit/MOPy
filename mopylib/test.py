from types import SimpleNamespace  

def plot(**orbits):
    all_orbits = {}
    orbit_name = {}
    for i,orbit in enumerate(orbits.items()):
        print(orbit)
        all_orbits[f'orbit_{i}'] = orbit[1]
        orbit_name[f'orbit_{i}'] = orbit[0]      
        
    # for key, value in all_orbits.items():
    #     print(f'{key:10}> {value}')
    return all_orbits, orbit_name


orbitss = {'orbit_1': {
                'radius_of_apogee': 125, 'radius_of_perigee': 00000, 
                'semi_major_axis': 00000, 'eccentricity': 00000, 
                'start_end_angle':[0, 2], 'orbit_resolution':1000
                },
           'orbit_2': {
                'radius_of_apogee': 895, 'radius_of_perigee': 1111, 
                'semi_major_axis': 13232, 'eccentricity': 1112, 
                'start_end_angle':[0, 2], 'orbit_resolution':1000
                }
           }

# orbit_01 = {
#                 'radius_of_apogee': 125, 'radius_of_perigee': 00000, 
#                 'semi_major_axis': 00000, 'eccentricity': 00000, 
#                 'start_end_angle':[0, 2], 'orbit_resolution':1000
#                 }

test_1, test_2 = plot(**orbitss)

for orbit_no, orbit in test_1.items():
    print(orbit.get('radius_of_apogee'))
    # print(test_1.get('orbit_0', None))

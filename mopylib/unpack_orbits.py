def unpack_orbits(**orbits: dict):
    orbit_details = {}
    orbit_names = {}
    for i, orbit in enumerate(orbits.items()):
        orbit_details[f'orbit_{i}'] = orbit[1]
        orbit_names[f'orbit_{i}'] = orbit[0]

    return orbit_details, orbit_names

if __name__ == '__main__':
    test_orbits = {'initial': {
                        'radius_of_apogee': 15000, 'radius_of_perigee': 10000,
                        # 'semi_major_axis': None, 'eccentricity': None,
                        'orbit_color': 'orange',
                        # 'start_angle':0, 'end_angle': 2, 'orbit_resolution':1000
                    },              
                        'transfer_1': {
                            'radius_of_apogee': 30000, 'radius_of_perigee': 10000,
                            'orbit_color': 'yellow',
                            'start_angle':0, 'end_angle': 2, 'orbit_resolution':1000    
                        },
                        
                        'final': {
                            'radius_of_apogee': 35000, 'radius_of_perigee': 30000
                        },
                    }
    
    orbit_details, orbit_names = unpack_orbits(**test_orbits)
    for keys, values in orbit_details.items():
        print(f'{keys}')
        for key, value in values.items():
            print(f'\t{key:20}= {value}')
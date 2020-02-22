from geopy.geocoders import Nominatim


def get_location_info(coordinates):
    try:
        geolocator = Nominatim(user_agent="specify_your_app_name_here")
        location = geolocator.reverse(f'{coordinates[0]}, {coordinates[1]}')
        return location.address
    except Exception as e:
        return 'Ошибка {0}'.format(e)

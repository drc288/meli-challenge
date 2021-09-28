from geopy import Nominatim

import math


def calculate_distance(country: str):
    """
    Calculate the distance from Buenos Aires Argentina to any other country
    :param country: any other country
    :return: distance in km
    """
    radians = math.pi / 180
    buenos_aires_location = (-34.602240, -58.456303)
    geolocation = Nominatim(user_agent="drc288")
    location = geolocation.geocode(country)

    # Get dif latitudes and longitudes
    dlat = location.latitude - buenos_aires_location[0]
    dlon = location.longitude - buenos_aires_location[1]

    # Earth radius
    r = 6372.795477598
    a = (math.sin(radians * dlat / 2)) ** 2 + math.cos(radians * buenos_aires_location[0]) * math.cos(
        radians * location.latitude) * (math.sin(radians * dlon / 2)) ** 2
    distance = 2 * r * math.asin(math.sqrt(a))
    return int(distance)

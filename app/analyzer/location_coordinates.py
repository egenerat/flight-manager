from lib.geopy import Nominatim
from lib.geopy.distance import vincenty

# https://pypi.python.org/pypi/geopy/1.11.0
# https://www.distancecalculator.net/about.php

class LocationCoordinates:

    def __init__(self):
        self.geolocator = Nominatim()

    def coordinates_city(self, city_name):
        return self.geolocator.geocode(city_name)

    def distance_2_points(self, city1, city2):
        # city1 = self.geolocator.geocode(city1)
        # print((city1.latitude, city1.longitude))
        # city2 = self.geolocator.geocode(city2)
        # if city1 and city2:
        lat1, long1 = city1
        lat2, long2 = city2
        return int(vincenty((lat1, long1), (lat2, long2)).km)
            # return int(great_circle((city1.latitude, city1.longitude), (city2.latitude, city2.longitude)).km)
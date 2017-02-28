from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from geopy.distance import great_circle

# https://pypi.python.org/pypi/geopy/1.11.0
# https://www.distancecalculator.net/about.php



def distance_2_points(city1, city2):
	geolocator = Nominatim()
	city1 = geolocator.geocode(city1)
	# print((paris.latitude, paris.longitude))
	city2 = geolocator.geocode(city2)
	# print((miami.latitude, miami.longitude))
	return int(vincenty((city1.latitude, city1.longitude), (city2.latitude, city2.longitude)).km)
	# print(great_circle((city1.latitude, city1.longitude), (city2.latitude, city2.longitude)).km)

def coordinates_city(city_name):
	geolocator = Nominatim()
	location = geolocator.geocode(city_name)
	return location

if __name__ == '__main__':
	geolocator = Nominatim()
	location = geolocator.reverse("52.509669, 13.376294")
	print(location.address)

	location = geolocator.geocode("175 5th Avenue NYC")
	print(location.address)
	# Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
	print((location.latitude, location.longitude))
	# (40.7410861, -73.9896297241625)

	city1 = "Le caire airport"
	city2 = "Miami international airport"
	distance_2_points(city1, city2)


	city1 = "Cairo airport"
	city2 = "Lyon aeroport"
	distance_2_points(city1, city2)
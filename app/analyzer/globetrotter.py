import csv

from app.analyzer.airport_finder import AirportFinder
from app.analyzer.capital_finder import CapitalFinder
from app.analyzer.countryname_translator import CountryNameTranslator
from app.analyzer.data.data_filepath import ORIGIN_COUNTRIES_FILE, ORIGIN_COUNTRIES_PREPARED_FILE
from app.analyzer.location import Location
from app.analyzer.location_coordinates import LocationCoordinates


def get_origin_countries():
    with open(ORIGIN_COUNTRIES_FILE, 'r') as f:
        return [country.strip('\n') for country in f.readlines()]


def get_origin_countries_prepared():
    result = {}
    with open(ORIGIN_COUNTRIES_PREPARED_FILE, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            # Irlande,Dublin,53.4,-6.1
            if len(row) == 4:
                result[(row[1], row[0])] = (row[2], row[3])
    return result


def simulate_reputation_mission(mission_type, has_stopover, new_distance):
    factor = {
        '4': 0.063,
        '5': 0.075
    }[mission_type]
    if has_stopover:
        factor *= 0.25
    return new_distance * factor


def filter_top_n_missions(missions_list, number_results):
    missions_list.sort(key=lambda tup: tup[1], reverse=True)
    return missions_list[:number_results]


class Globetrotter:

    def __init__(self):
        self.fr_country_names = get_origin_countries()
        self.origin_airports_location = []
        self.translator = CountryNameTranslator()
        self.capital_finder = CapitalFinder()
        # self.airport_finder = AirportFinder()
        self.locator = LocationCoordinates()
        self.fr_loc = Location()

    def get_airports(self, english_countryname, english_cityname):
        return self.airports_dict.get((english_cityname, english_countryname))

    def location_en_city(self, en_city_name, en_country_name):
        # airports = self.airport_finder.get_airports(en_city_name, en_country_name)
        # airport_location = airports[0]
        # return airport_location
        # return self.fr_loc.get_location(en_city_name, en_country_name)
        return self.locator.coordinates_city('{} {}'.format(en_city_name, en_country_name))

    def location_fr_city(self, fr_city_name):
        return self.locator.coordinates_city(fr_city_name)

    def get_origin_airports_location(self):
        result = []
        from_cache = True
        if from_cache:
            result = get_origin_countries_prepared()
        else:
            for fr_country_name in self.fr_country_names:
                en_country_name = self.translator.translate_country_name(fr_country_name)
                en_capital = self.capital_finder.get_capital(en_country_name)
                result.append((fr_country_name, en_capital, self.location_en_city(en_capital, en_country_name)))
        return result


def prepare_origin_countries_file():
    globetrotter = Globetrotter()
    origin_airports = globetrotter.get_origin_airports_location()
    with open(ORIGIN_COUNTRIES_PREPARED_FILE, 'w+') as f:
        for fr_country_name, en_capital_name in origin_airports:
            (latitude, longitude) = origin_airports.get((fr_country_name, en_capital_name))
            if latitude:
                f.write("{},{},{},{}\n".format(fr_country_name, en_capital_name, latitude, longitude))
            else:
                print("Could not find: {} {}".format(fr_country_name, en_capital_name))


if __name__ == '__main__':
    prepare_origin_countries_file()

import csv


# 1382,"Charles de Gaulle International Airport","Paris","France","CDG","LFPG",49.0127983093,2.54999995232,392,1,"E","Europe/Paris","airport","OurAirports"
def parse_airports():
    result = {}
    with open("app/analyzer/data/input/airports.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            result.setdefault((row[3], row[2]), []).append({
                    'airport_name': row[1],
                    'location': {
                        'latitude': row[6],
                        'longitude': row[7]
                    }
                })
    return result


class AirportFinder:

    def __init__(self):
        self.airports_dict = parse_airports()

    def get_airports(self, english_countryname, english_cityname):
        return self.airports_dict.get((english_cityname, english_countryname))

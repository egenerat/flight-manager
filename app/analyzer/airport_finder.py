import csv


from app.analyzer.data.data_filepath import AIRPORTS_CSV_FILE


def parse_airports():
    result = {}
    with open(AIRPORTS_CSV_FILE, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            result.setdefault((row[2], row[3]), []).append({
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

    def get_airports(self, english_cityname, english_countryname):
        return self.airports_dict.get((english_cityname, english_countryname))

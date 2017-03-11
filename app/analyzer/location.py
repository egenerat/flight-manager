import csv

from app.analyzer.data.data_filepath import DESTINATION_FILE


def parse_destination_file():
    result = {}
    with open(DESTINATION_FILE, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            # Irlande,Limerick,52.66,-8.64
            if len(row) == 4:
                result[(row[0], row[1])] = (row[2], row[3])
            else:
                print(row)
    return result


class Location:

    def __init__(self):
        self.destinations = parse_destination_file()

    def get_location(self, fr_city, fr_country):
        return self.destinations.get((fr_country, fr_city))

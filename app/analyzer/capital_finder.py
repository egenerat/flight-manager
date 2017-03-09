import csv


# "Austria","Vienna"
from app.analyzer.data.data_filepath import CAPITALS_CSV_FILE


def parse_country_capital():
    result = {}
    with open(CAPITALS_CSV_FILE, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            result[row[0]] = row[1]
    return result


class CapitalFinder:

    def __init__(self):
        self.capitals_dict = parse_country_capital()

    def get_capital(self, english_countryname):
        return self.capitals_dict.get(english_countryname)

import csv


# "Austria","Vienna"
def parse_country_capital():
    result = {}
    with open("app/analyzer/data/input/country-capital.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            result[row[0]] = row[1]
    return result


class CapitalFinder:

    def __init__(self):
        self.capitals_dict = parse_country_capital()

    def get_capital(self, english_countryname):
        return self.capitals_dict.get(english_countryname)

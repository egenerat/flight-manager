import csv

from app.analyzer.data.data_filepath import COUNTRIES_TRANSLATION_FILE


def parse_csv_countries_translation():
    result = {}
    with open(COUNTRIES_TRANSLATION_FILE, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            result[row[4]] = row[5]
    return result


class CountryNameTranslator:

    def __init__(self):
        self.country_name_translations = parse_csv_countries_translation()

    def translate_country_name(self, fr_country_name):
        return self.country_name_translations.get(fr_country_name)

# -*- coding: iso-8859-1 -*-
import requests

from app.airport.airports_parsers import get_country, get_money, get_kerosene_supply, get_kerosene_capacity, \
    get_engines_supply, get_planes_capacity, get_airport_name
from app.common.target_urls import MY_AIRPORT
import unittest


class TestAirportParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__html_page = requests.get(MY_AIRPORT).text

    def test_country(self):
        country = get_country(self.__html_page)
        self.assertEqual(country, 'France')

    def test_money(self):
        country = get_money(self.__html_page)
        self.assertEqual(country, 2444908)

    def test_kerosene_supply(self):
        country = get_kerosene_supply(self.__html_page)
        self.assertEqual(country, 2009391)

    def test_kerosene_capacity(self):
        country = get_kerosene_capacity(self.__html_page)
        self.assertEqual(country, 2500000)

    def test_engines_supply(self):
        engines_supply = get_engines_supply(self.__html_page)
        self.assertEqual(engines_supply['5'], 1000)
        self.assertEqual(engines_supply['6'], 2)

    def test_planes_capacity(self):
        country = get_planes_capacity(self.__html_page)
        self.assertEqual(country, 9)

    def test_airport_name(self):
        country = get_airport_name(self.__html_page)
        self.assertEqual(country, 'Roissy')


if __name__ == '__main__':
    unittest.main()

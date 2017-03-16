# -*- coding: utf-8 -*-

from app.airport.airports_parsers import get_country, get_money, get_kerosene_supply, get_kerosene_capacity, \
    get_engines_supply, get_planes_capacity, get_airport_name
from app.common.http_methods_unittests import get_request
from app.common.target_urls import MY_AIRPORT
import unittest


class TestAirportParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__html_page = get_request(MY_AIRPORT)

    def test_country(self):
        country = get_country(self.__html_page)
        self.assertEqual(u'Égypte', country)

    def test_money(self):
        country = get_money(self.__html_page)
        self.assertEqual(2444908, country)

    def test_kerosene_supply(self):
        country = get_kerosene_supply(self.__html_page)
        self.assertEqual(2009391, country)

    def test_kerosene_capacity(self):
        country = get_kerosene_capacity(self.__html_page)
        self.assertEqual(2500000, country)

    def test_engines_supply(self):
        engines_supply = get_engines_supply(self.__html_page)
        self.assertEqual(1000, engines_supply['5'])
        self.assertEqual(2, engines_supply['6'])

    def test_planes_capacity(self):
        country = get_planes_capacity(self.__html_page)
        self.assertEqual(9, country)

    def test_airport_name(self):
        country = get_airport_name(self.__html_page)
        self.assertEqual(u'Roissy aéroport', country)

if __name__ == '__main__':
    unittest.main()

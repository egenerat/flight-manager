# coding=utf-8
import requests

from app.airport.Airport import Airport
from app.common.target_urls import MY_AIRPORT
import unittest


class TestAirport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__html_page = requests.get(MY_AIRPORT).text

    def test_str(self):
        airport = Airport(country='Égypte',
                          money='123456',
                          kerosene_supply='',
                          kerosene_capacity='',
                          engines_supply='',
                          planes_capacity=84,
                          staff='',
                          airport_name='Aéroport égyptien')
        self.assertEqual('Airport Aéroport égyptien H84 Égypte', str(airport))

if __name__ == '__main__':
    unittest.main()

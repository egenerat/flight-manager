# -*- coding: utf-8 -*-
from app.airport.sale_airports_parser import build_airports_list
from app.common.http_methods_unittests import get_request
from app.common.target_urls import SALE_AIRPORT_TEST_URL
import unittest


class TestParserStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__html_page = get_request(SALE_AIRPORT_TEST_URL)

    def test_sale_airports(self):
        airports_list = build_airports_list(self.__html_page)
        self.assertEqual(2, len(airports_list))

        first_airport = airports_list[0]
        self.assertEqual(first_airport['airport_id'], 106982)
        self.assertEqual(first_airport['cash'], 1092038031)
        self.assertEqual(first_airport['capacity'], 41)
        self.assertEqual(first_airport['reputation'], 1784487)
        self.assertEqual(first_airport['price'], 8332773945)
        self.assertEqual(first_airport['vendor'], "Mix456")

if __name__ == '__main__':
    unittest.main()

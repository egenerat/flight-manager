# -*- coding: utf-8 -*-
from app.airport.sale_airports_parser import build_airports_list
from app.common.http_methods_unittests import get_request
from app.common.target_urls import SALE_1_AIRPORT_TEST_URL, SALE_2_AIRPORTS_TEST_URL
import unittest


class TestParserStaff(unittest.TestCase):

    def test_sale_1_airport(self):
        html_page = get_request(SALE_1_AIRPORT_TEST_URL)
        airports_list = build_airports_list(html_page)
        self.assertEqual(1, len(airports_list))

        first_airport = airports_list[0]
        self.assertEqual(first_airport['airport_id'], 128773)
        self.assertEqual(first_airport['cash'], 0)
        self.assertEqual(first_airport['capacity'], 27)
        self.assertEqual(first_airport['reputation'], 188124)
        self.assertEqual(first_airport['price'], 724145248)
        self.assertEqual(first_airport['vendor'], "Max333")

    def test_sale_2_airports(self):
        html_page = get_request(SALE_2_AIRPORTS_TEST_URL)
        airports_list = build_airports_list(html_page)
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

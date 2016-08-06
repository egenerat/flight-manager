# -*- coding: iso-8859-1 -*-
import requests

from app.airport.staff_parser import get_pilots, get_flight_attendants, get_mechanics
from app.common.target_urls import STAFF_PAGE_TEST
import unittest


class TestParserStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__html_page = requests.get(STAFF_PAGE_TEST).text

    def test_pilots(self):
        total_pilots, busy_pilots = get_pilots(self.__html_page)
        self.assertEqual(total_pilots, 166)
        self.assertEqual(busy_pilots, 148)

    def test_flight_attendants(self):
        total_flight_attendants, busy_flight_attendants = get_flight_attendants(self.__html_page)
        self.assertEqual(total_flight_attendants, 156)
        self.assertEqual(busy_flight_attendants, 136)

    def test_mechanics(self):
        self.assertEqual(get_mechanics(self.__html_page), 36)

if __name__ == '__main__':
    unittest.main()

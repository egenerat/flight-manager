# -*- coding: utf-8 -*-

from app.airport.staff_parser import get_pilots, get_flight_attendants, get_mechanics
from app.common.http_methods_unittests import get_request
from app.common.target_urls import STAFF_PAGE_TEST
import unittest


class TestParserStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__html_page = get_request(STAFF_PAGE_TEST)

    def test_pilots(self):
        total_pilots, busy_pilots = get_pilots(self.__html_page)
        self.assertEqual(166, total_pilots)
        self.assertEqual(148, busy_pilots)

    def test_flight_attendants(self):
        total_flight_attendants, busy_flight_attendants = get_flight_attendants(self.__html_page)
        self.assertEqual(156, total_flight_attendants)
        self.assertEqual(136, busy_flight_attendants)

    def test_mechanics(self):
        self.assertEqual(36, get_mechanics(self.__html_page))

if __name__ == '__main__':
    unittest.main()

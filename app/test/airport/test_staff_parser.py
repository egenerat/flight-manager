# -*- coding: iso-8859-1 -*-
import requests

from app.airport.staff_parser import get_pilotes, get_flight_attendants
from app.common.target_urls import STAFF_PAGE
import unittest


class TestParserStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__html_page = requests.get(STAFF_PAGE).text

    def test_pilotes(self):
        total_pilotes, busy_pilotes = get_pilotes(self.__html_page)
        self.assertEqual(total_pilotes, 166)
        self.assertEqual(busy_pilotes, 148)

    def test_flight_attendants(self):
        total_flight_attendants, busy_flight_attendants = get_flight_attendants(self.__html_page)
        self.assertEqual(total_flight_attendants, 156)
        self.assertEqual(busy_flight_attendants, 136)

if __name__ == '__main__':
    unittest.main()

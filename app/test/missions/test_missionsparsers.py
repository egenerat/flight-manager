# -*- coding: iso-8859-1 -*-

import requests

from app.common.target_strings import MISSION_DEPARTURE_TIME
from app.common.target_urls import YOUR_MISSIONS_URL
from app.missions.missionparser import parse_all_missions_in_page, parse_duration_before_departure
import unittest


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.html_page = requests.get(YOUR_MISSIONS_URL).text

    def test_parser(self):
        self.missions_list = parse_all_missions_in_page(self.html_page, '1')
        self.assertEqual(len(self.missions_list), 3)

    def test_truc(self):
        a = parse_duration_before_departure(MISSION_DEPARTURE_TIME)

if __name__ == '__main__':
    unittest.main()

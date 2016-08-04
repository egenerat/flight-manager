# -*- coding: iso-8859-1 -*-

import requests

from app.common.target_strings import MISSION_DEPARTURE_TIME
from app.common.target_urls import YOUR_MISSIONS_URL
from app.missions.missionparser import parse_all_missions_in_page, parse_duration_before_departure
import unittest


class TestParser(unittest.TestCase):

    def test_parser(self):
        self.html_page = requests.get(YOUR_MISSIONS_URL).text
        self.missions_list = parse_all_missions_in_page(self.html_page, '1')
        self.assertEqual(len(self.missions_list), 10)

    def test_truc(self):
        a = parse_duration_before_departure(MISSION_DEPARTURE_TIME)

    def test_jet_missions(self):
        html_page2 = requests.get("http://localhost/AS/vos-missions-jet.html").text
        missions_list = parse_all_missions_in_page(html_page2, '1')
        self.assertEqual(len(missions_list), 11)

if __name__ == '__main__':
    unittest.main()

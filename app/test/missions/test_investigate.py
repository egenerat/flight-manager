# -*- coding: utf-8 -*-
from app.common.http_methods_unittests import get_request
from app.missions.investigate_crash import parse_flights_overview, flights_overview
import unittest


class TestParser(unittest.TestCase):

    @unittest.skip("Need to clean first source file")
    def test_feasible(self):
        html_page = get_request(flights_overview)
        results = parse_flights_overview(html_page)
        self.assertEqual(len(results), 1)
        flight_failed = results[0]
        self.assertEqual(flight_failed['mission_id'], '2212')
        self.assertEqual(flight_failed['country_id'], '36')
        self.assertEqual(flight_failed['country_name'], u'Burkina Faso')
        self.assertEqual(flight_failed['details_link'], u'compte.php?page=carnet-vol1&id_m=783')
        self.assertTrue(flight_failed['last_message'], u"Mauvaise météo, la Neige s'abbat sur votre aéroport...")


if __name__ == '__main__':
    unittest.main()

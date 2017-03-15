# coding=utf-8

from app.common.http_methods_unittests import get_request
from app.common.target_urls import YOUR_MISSIONS_URL, YOUR_MISSIONS_JET_URL
from app.missions.missionparser import parse_all_missions_in_page, parse_stopover
import unittest


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.html_page = get_request(YOUR_MISSIONS_URL)
        cls.missions_list = parse_all_missions_in_page(cls.html_page, '1')

    def test_parser(self):
        self.html_page = get_request(YOUR_MISSIONS_URL)
        self.missions_list = parse_all_missions_in_page(self.html_page, '1')
        self.assertEqual(10, len(self.missions_list))

    def test_nb_missions_page(self):
        self.assertEqual(10, len(self.missions_list))

    def test_jet_missions(self):
        html_page2 = get_request(YOUR_MISSIONS_JET_URL)
        missions_list = parse_all_missions_in_page(html_page2, '1')
        self.assertEqual(11, len(missions_list))

    def test_simple_mission(self):
        simple_mission = self.missions_list[3]
        self.assertEqual(1, simple_mission['country_nb'])
        self.assertEqual(378, simple_mission['mission_nb'])
        self.assertEqual(504, simple_mission['travellers_nb'])
        self.assertEquals('Edmonton', simple_mission['city_name'])
        self.assertEqual(287040, simple_mission['contract_amount'])
        self.assertEqual(152, simple_mission['reputation'])
        self.assertEqual(3, simple_mission['pilots_nb'])
        self.assertEqual(1, simple_mission['flight_attendants_nb'])
        self.assertFalse(simple_mission['stopover'])
        # TODO find a solution to mock current time
        # self.assertEqual(1, simple_mission['time_before_departure'])
        self.assertEqual(7568, simple_mission['km_nb'])

    def test_mission_stopover(self):
        stopover_mission = self.missions_list[4]
        stopover_details = stopover_mission['stopover']
        self.assertTrue(stopover_details)

    def test_stopover(self):
        stopover_html = get_request("http://localhost/test_pages/stopover_details.html")
        a_stopover = parse_stopover(stopover_html)
        self.assertEqual(29, a_stopover['reputation'])
        self.assertEqual(7, a_stopover['travellers_nb'])
        self.assertEqual(25930, a_stopover['revenue'])

if __name__ == '__main__':
    unittest.main()

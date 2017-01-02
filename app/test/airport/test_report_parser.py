# -*- coding: iso-8859-1 -*-
import requests

from app.airport.report_parser import report_parser
from app.common.target_urls import REPORT_URL
import unittest


class TestParserStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__html_page = requests.get(REPORT_URL).text

    def test_daily_crashes(self):
        daily_crashes = report_parser(self.__html_page)['daily']['crashes']
        self.assertEqual(1234, daily_crashes)

if __name__ == '__main__':
    unittest.main()

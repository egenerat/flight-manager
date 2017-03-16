# -*- coding: utf-8 -*-

from app.airport.report_parser import report_parser
from app.common.http_methods_unittests import get_request
from app.common.target_urls import REPORT_URL
import unittest


class TestParserStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__html_page = get_request(REPORT_URL)

    def test_daily_crashes(self):
        daily_crashes = report_parser(self.__html_page)['daily']['crashes']
        self.assertEqual(1234, daily_crashes)

if __name__ == '__main__':
    unittest.main()

import unittest

import requests

from app.standalone.PlaneSpecificationParser import PlaneSpecificationParser


class TestPlanesUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html_page = requests.get("http://172.17.0.1/test_pages/planes_shop_3rf_page_details.html").text
        cls.parser = PlaneSpecificationParser(html_page)

    def test_get_engine_nb(self):
        self.assertEqual(self.parser.get_engine_nb(), 2)

if __name__ == '__main__':
    unittest.main()

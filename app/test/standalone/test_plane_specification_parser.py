import unittest

from app.common.http_methods_unittests import get_request
from app.standalone.PlaneSpecificationParser import PlaneSpecificationParser


class TestPlanesUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html_page = get_request("http://172.17.0.1/test_pages/planes_shop_3rf_page_details.html")
        cls.parser = PlaneSpecificationParser(html_page=html_page)

    def test_get_engine_nb(self):
        self.assertEqual(self.parser.get_engine_nb(), 2)

    def test_get_plane_model(self):
        self.assertEqual(self.parser.get_plane_model(), u"Falcon 2000 EX")

    def test_get_speed(self):
        self.assertEqual(self.parser.get_speed(), 850)

    def test_get_kerosene_capacity(self):
        self.assertEqual(self.parser.get_kerosene_capacity(), 9400)

    def test_get_kerosene_consumption(self):
        self.assertEqual(self.parser.get_kerosene_consumption(), 1135)

    def test_get_price(self):
        self.assertEqual(self.parser.get_price(), 1850000)


if __name__ == '__main__':
    unittest.main()

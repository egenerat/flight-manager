import unittest

from app.alliance.alliance_parser import AllianceParser
from app.common.http_methods_unittests import get_request


class TestAllianceParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html_page = get_request("http://172.17.0.1/test_pages/planes_shop_3rf_page_details.html")
        cls.parser = AllianceParser(html_page=html_page)

    @unittest.skip("Not implemented yet")
    def test_get_engine_nb(self):
        self.assertEqual(self.parser.get_engine_nb(), 2)


if __name__ == '__main__':
    unittest.main()

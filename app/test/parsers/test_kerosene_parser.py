from app.common.http_methods_unittests import get_request
from app.common.target_urls import KEROSENE_SHOP_URL
from app.parsers.kerosene_parser import extract_information
import unittest


class TestKeroseneParser(unittest.TestCase):

    def test_kerosene_shop_parser(self):
        html_page = get_request(KEROSENE_SHOP_URL)
        result = extract_information(html_page)
        self.assertEqual(3.01, result['price_per_litre'])
        self.assertEqual(11500530244, result['units_available'])


if __name__ == '__main__':
    unittest.main()

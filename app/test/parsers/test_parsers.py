import requests

from app.common.target_urls import YOUR_PLANES_URL
from app.parsers.planesparser import is_regular_plane, build_planes_from_html
import unittest


class TestPlaneType(unittest.TestCase):

    def test_777_regular(self):
        self.assertTrue(is_regular_plane('B777-200ER'))

    def test_concorde_regular(self):
        self.assertFalse(is_regular_plane('Concorde'))


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.html_page = requests.get(YOUR_PLANES_URL).text

    def test_parser(self):
        planes_list = build_planes_from_html(self.html_page)
        print(len(planes_list))
        self.assertEqual(len(planes_list), 186)

if __name__ == '__main__':
    unittest.main()

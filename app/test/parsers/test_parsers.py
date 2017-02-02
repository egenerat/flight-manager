from app.common.http_methods_unittests import get_request
from app.common.target_urls import YOUR_PLANES_URL
from app.parsers.planes_parser import build_planes_from_html
import unittest

from app.planes.planes_util import is_regular_plane
from app.planes.planes_util2 import split_planes_list_by_type


class TestPlaneType(unittest.TestCase):

    def test_777_regular(self):
        self.assertTrue(is_regular_plane('B777-200ER'))

    def test_concorde_regular(self):
        self.assertFalse(is_regular_plane('Concorde'))


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.html_page = get_request(YOUR_PLANES_URL)

    def test_parser(self):
        # 97 Concorde
        #   all active
        # 89 777
        #   all inactive
        #   20 in maintenance
        self.planes_list = build_planes_from_html(self.html_page)
        self.assertEqual(186, len(self.planes_list))
        planes_by_type = split_planes_list_by_type(self.planes_list)
        self.assertEqual(97, len(planes_by_type['supersonic_planes']))
        self.assertEqual(89, len(planes_by_type['commercial_planes']))
        self.assertEqual(0, len(planes_by_type['supersonic_ready_planes']))
        self.assertEqual(69, len(planes_by_type['commercial_ready_planes']))

    def test_parser(self):
        html_page = get_request("http://localhost/test_pages/your_planes_no_plane.html")
        self.planes_list = build_planes_from_html(html_page)
        self.assertEqual(0, len(self.planes_list))

if __name__ == '__main__':
    unittest.main()

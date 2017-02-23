from app.planes.commercial7plane4 import Commercial7Plane4
from app.parsers.planes_parser import build_plane_from_line
import unittest

from app.test.parsers.resources_planes_html import plane_in_maintenance


class TestParserOnePlane(unittest.TestCase):

    def test_plane_in_maintenance(self):
        self.plane = build_plane_from_line(plane_in_maintenance)
        self.assertEqual(Commercial7Plane4, type(self.plane))
        self.assertFalse(self.plane.ready)


if __name__ == '__main__':
    unittest.main()

from app.planes.Commercial7Plane import Commercial7Plane
from app.parsers.planes_parser import build_plane_from_line
import unittest

from app.test.parsers.resources_planes_html import plane_in_maintenance


class TestParserOnePlane(unittest.TestCase):

    def test_plane_in_maintenance(self):
        self.plane = build_plane_from_line(plane_in_maintenance)
        self.assertEqual(type(self.plane), Commercial7Plane)
        self.assertEqual(self.plane.ready, False)


if __name__ == '__main__':
    unittest.main()

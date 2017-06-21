from app.planes.commercial7plane4 import Commercial7Plane4
from app.parsers.planes_parser import build_plane_from_line
import unittest

from app.test.parsers.resources_planes_html import plane_in_maintenance, plane_active_maintenance_needed


class TestParserOnePlane(unittest.TestCase):

    def test_plane_in_maintenance(self):
        plane = build_plane_from_line(plane_in_maintenance)
        self.assertEqual(Commercial7Plane4, type(plane))
        self.assertFalse(plane.ready)

    def test_plane_maintenance_needed_active(self):
        plane = build_plane_from_line(plane_active_maintenance_needed)
        self.assertFalse(plane.ready)
        self.assertEqual('A', plane.in_mission)

if __name__ == '__main__':
    unittest.main()

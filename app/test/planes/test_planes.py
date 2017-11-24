import unittest

from app.planes.commercial7plane4 import Commercial7Plane4
from app.planes.jet_gx_plane import JetGXPlane


class TestParser(unittest.TestCase):
    def test_no_maintenance(self):
        plane = Commercial7Plane4(plane_id='123', required_maintenance=True, ready=True, kerosene=0,
                                  current_engine_hours=20, maximum_engine_hours=75, km=250000, in_mission=False)
        self.assertFalse(plane.engines_to_be_changed())

    def test_maintenance(self):
        plane = Commercial7Plane4(plane_id='123', required_maintenance=True, ready=True, kerosene=0,
                                  current_engine_hours=74, maximum_engine_hours=75, km=250000, in_mission=False)
        self.assertTrue(plane.engines_to_be_changed())

    def test_no_maintenance_jet(self):
        plane = JetGXPlane(plane_id='123', required_maintenance=True, ready=True, kerosene=0,
                           current_engine_hours=44, km=250000, in_mission=False)
        self.assertFalse(plane.engines_to_be_changed())

    def test_maintenance_jet(self):
        plane = JetGXPlane(plane_id='123', required_maintenance=True, ready=True, kerosene=0,
                           current_engine_hours=65, km=250000, in_mission=False)
        self.assertTrue(plane.engines_to_be_changed())

    def test_range_jet(self):
        plane_class = JetGXPlane
        self.assertEqual(6335, plane_class.plane_range)


if __name__ == '__main__':
    unittest.main()

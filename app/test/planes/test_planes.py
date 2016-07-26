import unittest

from app.planes.JetPlane import JetPlane
from app.planes.UsableCommercialPlane import UsableCommercialPlane
from app.planes.UsableJetPlane import UsableJetPlane


class TestParser(unittest.TestCase):
    def test_no_maintenance(self):
        plane = UsableCommercialPlane(plane_id='123', required_maintenance=True, ready=True, kerosene=0,
                                      current_engine_hours=20, maximum_engine_hours=75, km=250000)
        self.assertFalse(plane.engines_to_be_changed())

    def test_maintenance(self):
        plane = UsableCommercialPlane(plane_id='123', required_maintenance=True, ready=True, kerosene=0,
                                      current_engine_hours=74, maximum_engine_hours=75, km=250000)
        self.assertTrue(plane.engines_to_be_changed())

    def test_no_maintenance_jet(self):
        plane = UsableJetPlane(plane_id='123', required_maintenance=True, ready=True, kerosene=0,
                               current_engine_hours=44, km=250000)
        self.assertFalse(plane.engines_to_be_changed())

    def test_maintenance_jet(self):
        plane = UsableJetPlane(plane_id='123', required_maintenance=True, ready=True, kerosene=0,
                               current_engine_hours=65, km=250000)
        self.assertTrue(plane.engines_to_be_changed())

    def test_range_jet(self):
        plane_class = JetPlane
        self.assertTrue(plane_class.plane_range, 9999)


if __name__ == '__main__':
    unittest.main()

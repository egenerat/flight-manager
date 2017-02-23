# coding=utf-8

from app.missions.mission import is_mission_feasible
import unittest

from app.planes.supersonic_tu_plane import SupersonicTUPlane


class TestMission(object):
    def __init__(self, **kwargs):
        self.km_nb = kwargs['km_nb']
        self.travellers_nb = kwargs['travellers_nb']
        self.pilots_nb = kwargs['pilots_nb']
        self.flight_attendants_nb = kwargs['flight_attendants_nb']


class TestParser(unittest.TestCase):

    def test_feasible(self):
        mission = TestMission(km_nb=4000, travellers_nb=0, pilots_nb=0, flight_attendants_nb=0)
        plane = SupersonicTUPlane(plane_id=0, ready=True)
        self.assertTrue(is_mission_feasible(mission, plane))

    def test_not_feasible(self):
        mission = TestMission(km_nb=5000, travellers_nb=0, pilots_nb=0, flight_attendants_nb=0)
        plane = SupersonicTUPlane(plane_id=0, ready=True)
        self.assertFalse(is_mission_feasible(mission, plane))

if __name__ == '__main__':
    unittest.main()

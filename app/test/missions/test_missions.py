# -*- coding: iso-8859-1 -*-

from app.common.constants import CONCORDE_SPEED
from app.missions.mission import hours_consumed
import unittest


class TestMission(unittest.TestCase):

    def test_duration_mission(self):
        missions_hours = hours_consumed(10000, CONCORDE_SPEED)
        self.assertEqual(missions_hours, 5)

if __name__ == '__main__':
    unittest.main()

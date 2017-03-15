# coding=utf-8
import unittest

from app.analyzer.location_coordinates import LocationCoordinates


class TestCapitalFinder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.locator = LocationCoordinates()

    def test_get_amount(self):
        loc1 = (1.000, 2.000)
        loc2 = (3.000, 4.000)
        self.assertEqual(self.locator.distance_2_points(loc1, loc2), 313)


if __name__ == '__main__':
    unittest.main()

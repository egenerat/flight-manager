# coding=utf-8
import unittest

from app.analyzer.location_coordinates import LocationCoordinates


class TestCapitalFinder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.locator = LocationCoordinates()

    def test_get_amount(self):
        self.assertEqual(self.locator.distance_2_points("Cairo airport", "Lyon aeroport"), 7450)


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
import unittest

from app.analyzer.airport_finder import AirportFinder


@unittest.skip("demonstrating skipping")
class TestAirportFinder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.finder = AirportFinder()

    def test_get_amount(self):
        self.assertEqual(len(self.finder.get_airports("Paris", "France")), 3)


if __name__ == '__main__':
    unittest.main()

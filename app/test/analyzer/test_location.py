# coding=utf-8
import unittest

from app.analyzer.location import Location


class TestCapitalFinder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.locator = Location()

    def test_get_amount(self):
        self.assertEqual(self.locator.get_location("Limerick", "Irlande"), 7450)


if __name__ == '__main__':
    unittest.main()

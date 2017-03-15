# coding=utf-8
import unittest

from app.analyzer.location import Location


class TestLocation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.locator = Location()

    def test_get_amount(self):
        self.assertEqual(self.locator.get_location("Limerick", "Irlande"), ('52.661252','-8.6301238'))


if __name__ == '__main__':
    unittest.main()

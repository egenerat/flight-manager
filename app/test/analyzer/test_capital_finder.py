# coding=utf-8
import unittest

from app.analyzer.capital_finder import CapitalFinder


class TestCapitalFinder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.finder = CapitalFinder()

    def test_get_amount(self):
        self.assertEqual(self.finder.get_capital("Austria"), "Vienna")


if __name__ == '__main__':
    unittest.main()

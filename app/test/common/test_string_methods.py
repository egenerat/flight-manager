# -*- coding: utf-8 -*-
import unittest

from app.common.string_methods import get_amount, clean_amount


class TestStringMethods(unittest.TestCase):

    def test_large_amount(self):
        string = "-10,198,127 $"
        self.assertEqual(-10198127, get_amount(string))
        self.assertEqual(-10198127, clean_amount(string))


    def test_one_digit(self):
        string = "3"
        self.assertEqual(3, get_amount(string))
        self.assertEqual(3, clean_amount(string))


    def test_negative(self):
        string = "-260,410"
        self.assertEqual(-260410, get_amount(string))
        self.assertEqual(-260410, clean_amount(string))


if __name__ == '__main__':
    unittest.main()

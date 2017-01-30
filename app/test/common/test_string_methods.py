# coding=utf-8
import unittest

from app.common.string_methods import get_amount


class TestStringMethods(unittest.TestCase):

    def test_get_amount(self):
        string = "-10,198,127 $"
        self.assertEqual(get_amount(string), -10198127)


if __name__ == '__main__':
    unittest.main()

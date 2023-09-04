import unittest

from lab1 import max_value


class Task1MaxTest(unittest.TestCase):
    def test_max_value_empty_list(self):
        self.assertEqual(None, max_value([]))

    def test_max_value_list_with_one_entry(self):
        self.assertEqual(321, max_value([321]))

    def test_max_value_list_with_multiple_entries(self):
        self.assertEqual(3201, max_value([1023, 456, 123, 3201, 890]))
        self.assertEqual(10230, max_value([10230, 456, 123, 3201, 890]))
        self.assertEqual(89000, max_value([10230, 456, 123, 3201, 89000]))

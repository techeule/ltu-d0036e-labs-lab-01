import unittest

from lab1 import min_value


class Task1MinTest(unittest.TestCase):
    def test_min_value_empty_list(self):
        self.assertEqual(None, min_value([]))

    def test_min_value_list_with_one_entry(self):
        self.assertEqual(321, min_value([321]))

    def test_min_value_list_with_multiple_entries(self):
        self.assertEqual(123, min_value([3201, 1023, 456, 123, 890]))
        self.assertEqual(123, min_value([3201, 1023, 456, 890, 123]))
        self.assertEqual(123, min_value([123, 3201, 1023, 456, 890]))

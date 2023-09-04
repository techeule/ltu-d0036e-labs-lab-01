import unittest

from lab1 import mean_value


class Task1MeanTest(unittest.TestCase):
    def test_mean_value_empty_list(self):
        self.assertEqual(None, mean_value([]))

    def test_mean_value_list_with_one_entry(self):
        self.assertEqual(321, mean_value([321]))

    def test_mean_value_list_with_multiple_entries(self):
        numbers = [1023, 456, 123, 3201, 890]
        sum_of = sum(numbers)
        mean = sum_of / len((numbers))
        self.assertEqual(mean, mean_value(numbers))

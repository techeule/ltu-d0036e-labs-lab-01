import unittest
from functools import reduce

from lab1 import mean_value, variance_value


class Task1VarianceTest(unittest.TestCase):
    def test_variance_value_empty_list(self):
        self.assertEqual(None, variance_value([]))

    def test_variance_value_list_with_one_entry(self):
        self.assertEqual(321, variance_value([321]))

    def test_variance_value_list_with_multiple_entries(self):
        numbers = [600, 470, 170, 430, 300]
        number_entry_count = len(numbers)
        mean = mean_value(numbers)
        reduced = reduce(lambda x, y: x + y, [(mean - x) ** 2 for x in numbers])
        variance_of = reduced / number_entry_count
        self.assertEqual(variance_of, variance_value(numbers))

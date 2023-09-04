import unittest
from functools import reduce
from math import sqrt

from lab1 import mean_value, std_deviation_value


class Task1StandardDeviationTest(unittest.TestCase):
    def test_std_deviation_value_empty_list(self):
        self.assertEqual(None, std_deviation_value([]))

    def test_std_deviation_value_list_with_one_entry(self):
        self.assertEqual(sqrt(321), std_deviation_value([321]))

    def test_std_deviation_value_list_with_multiple_entries(self):
        numbers = [600, 470, 170, 430, 300]
        number_entry_count = len(numbers)
        mean = mean_value(numbers)
        reduced = reduce(lambda x, y: x + y, [(mean - x) ** 2 for x in numbers])
        std_dev = sqrt(reduced / number_entry_count)
        self.assertEqual(std_dev, std_deviation_value(numbers))

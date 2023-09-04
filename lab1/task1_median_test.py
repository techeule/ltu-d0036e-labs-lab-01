import unittest

from lab1 import median_value


class Task1MedianTest(unittest.TestCase):
    def test_median_value_empty_list(self):
        self.assertEqual(None, median_value([]))

    def test_median_value_list_with_one_entry(self):
        self.assertEqual(321, median_value([321]))

    def test_median_value_list_with_multiple_entries_odd_number_of_elements(self):
        numbers = [600, 470, 170, 430, 300]  # 170, 300, 430, 470, 600
        self.assertEqual(430, median_value(numbers))

    def test_median_value_list_with_multiple_entries_even_number_of_elements(self):
        numbers = [170, 300, 390, 430, 470, 600]  # 170, 300, 390, 430, 470, 600
        self.assertEqual((390 + 430) / 2, median_value(numbers))

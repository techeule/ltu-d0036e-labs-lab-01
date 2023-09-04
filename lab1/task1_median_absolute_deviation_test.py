import unittest

from lab1 import median_value, median_abs_dev_value


class Task1MedianAbsoluteDeviationTest(unittest.TestCase):
    def test_median_abs_dev_value_empty_list(self):
        self.assertEqual(None, median_abs_dev_value([]))

    def test_median_abs_dev_value_list_with_one_entry(self):
        self.assertEqual(0, median_abs_dev_value([321]))

    def test_median_abs_dev_value_list_with_multiple_entries_odd_number_of_elements(self):
        numbers = [600, 470, 170, 430, 300]  # [170, 300, 430, 470, 600]
        media = median_value(numbers)
        abs_diff = [abs(x - media) for x in numbers]
        median_abs_dev = median_value(abs_diff)
        self.assertEqual(median_abs_dev, median_abs_dev_value(numbers))

    def test_median_abs_dev_value_list_with_multiple_entries_even_number_of_elements(self):
        numbers = [170, 300, 390, 430, 470, 600]  # [170, 300, 390, 430, 470, 600]
        media = median_value(numbers)
        abs_diff = [abs(x - media) for x in numbers]
        median_abs_dev = median_value(abs_diff)
        self.assertEqual(median_abs_dev, median_abs_dev_value(numbers))

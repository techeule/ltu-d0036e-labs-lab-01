import unittest

from lab1 import load_plain_csv, load_dataframe_csv


class LoadCsvTest(unittest.TestCase):
    def test_load_csv_default_args(self):
        csv_lines = load_plain_csv("example.csv")
        self.assertEqual(8, len(csv_lines))

    def test_load_csv_as_dataframe(self):
        csv_dataframe = load_dataframe_csv("example.csv")
        describe = csv_dataframe.describe()
        self.assertEqual(10, len(describe.columns))
        self.assertEqual(7, len(csv_dataframe))

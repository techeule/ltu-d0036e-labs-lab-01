import os

import pandas as pd
from pandas import DataFrame


def load_plain_csv(path, delimiter=','):
    rows = []
    with open(path) as csv_file:
        for line in csv_file:
            rows.append(line.strip().split(delimiter))
    return rows


def load_dataframe_csv(path, delimiter=',') -> DataFrame:
    csv_lines = load_plain_csv(path, delimiter)
    return pd.DataFrame(csv_lines[1:], columns=csv_lines[0])


if __name__ == '__main__':
    HERE = os.path.dirname(__file__)
    print("housing\n", load_dataframe_csv(os.path.join(HERE, "..", "docs", "Lab 1", "housing.csv")))

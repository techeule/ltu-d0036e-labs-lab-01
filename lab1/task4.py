import os

import matplotlib.pyplot as plt
from pandas import DataFrame

from lab1 import load_dataframe_csv, mean_value

MIN_BINS = 10

HERE = os.path.dirname(__file__)


def count_rows(dataframe: DataFrame) -> int:
    values = dataframe.shape
    return values[0]


class Task4:
    def __init__(self, path):
        self.path = path
        self.dataframe = load_dataframe_csv(path)

    def column_names(self):
        return self.dataframe.columns.to_list()

    def subtask_1(self):
        return self.dataframe.shape[0]

    def subtask_2(self) -> float:
        house_values = self.dataframe['median_house_value'].astype(float).to_list()
        return mean_value(house_values)

    def subtask_3(self, column_names=[], bins=MIN_BINS, file=None):
        histograms = {}
        if column_names is None or column_names is []:
            return histograms

        if type(bins) != int or bins < MIN_BINS:
            bins = MIN_BINS

        self.dataframe[column_names].astype(float).hist(bins=bins)
        plt.show()
        if file is not None:
            plt.savefig(**file)

    def subtask_4(self):

        max_housing_median_age = self.dataframe['housing_median_age'].astype(float).max()
        number_of_housing_median_age_with_max = len(
            self.dataframe[self.dataframe['housing_median_age'].astype(float) == max_housing_median_age])

        max_median_house_value = self.dataframe['median_house_value'].astype(float).max()
        number_of_median_house_value_with_max = len(
            self.dataframe[self.dataframe['median_house_value'].astype(float) == max_median_house_value])

        return f"""
        The histograms of 'housing_median_age' and 'median_house_value' show an anomaly.
        The last elements on the X-axis show a very high number.
        housing_median_age 
            max = {max_housing_median_age} and
            number of district with max housing_median_age = {number_of_housing_median_age_with_max}.
        
        median_house_value
            max = {max_median_house_value} and, 
            number of district with max median_house_value = {number_of_median_house_value_with_max}.
        """

    def subtask_additional_task_1(self):
        attribute = 'ocean_proximity'
        ocean_proximity_categories = set()
        for ocean_proximity in self.dataframe[attribute].to_list():
            ocean_proximity_categories.add(ocean_proximity)

        mean_house_value_by_category = dict()
        for ocean_proximity in ocean_proximity_categories:
            median_house_hold_df = self.dataframe[self.dataframe[attribute] == ocean_proximity]['median_house_value']
            median_house_hold = median_house_hold_df.astype(float)
            if median_house_hold.mean() != mean_value(median_house_hold.to_list()):
                raise Exception("expected median_house_hold.mean() == mean_value(median_house_hold.to_list())")
            mean_house_value_by_category[ocean_proximity] = mean_value(median_house_hold.to_list())

        return mean_house_value_by_category

    def subtask_6(self):
        return """
        """


if __name__ == '__main__':
    root_path = os.path.join(HERE, "..")
    root_path = os.path.abspath(root_path)
    output_file_from_4_3 = os.path.join(root_path, "task_4_subtask_3.png")

    housing_file_path = os.path.join(root_path, "docs", "Lab 1", "housing.csv")
    housing_file_path = os.path.abspath(housing_file_path)
    print(f"housing_file_path='{housing_file_path}'")

    task4 = Task4(housing_file_path)

    print(f"Columns\n\t{task4.column_names()}")
    # Task 4.1
    print(f"the number of districts loaded in this exercise\n\t{task4.subtask_1()}")

    # Task 4.2
    print(f"the mean of house values among all the districts\n\t{'{:.3f}'.format(task4.subtask_2())}")

    # Task 4.3
    attributes = ['households', 'median_income', 'housing_median_age', 'median_house_value']
    print(f"Create a histogram for\n\t{attributes}")
    task4.subtask_3(column_names=attributes, bins=250)

    # Task 4.4 and
    # Task 4.5
    print(f"What do you notice about the graphs? Specifically focus on end of housing_median_age and "
          f"median_house_value graphs.\n\t{task4.subtask_4()}")

    # Task 4.5.Additional Task
    print(f"For each ocean proximity category in the dataset calculate the mean house value")
    mean_house_value_by_ocean_proximity = task4.subtask_additional_task_1()
    for entry, value in mean_house_value_by_ocean_proximity.items():
        print("\t{:<14} {:<30}".format(entry, value))

    print(f"Think about the following two cases:\n\t{task4.subtask_6()}")

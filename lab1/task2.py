from lab1 import min_value, max_value, mean_value, std_deviation_value, median_value, median_abs_dev_value

grades = [8, 6, 1, 7, 8, 9, 8, 7, 10, 7, 6, 9, 7]


def print_pretty(function_name, numeric_list, final_value, description=None):
    print(f"\n\n{final_value} is the {function_name} of {numeric_list}\n\tdescription:\n\t{description}")


if __name__ == "__main__":
    print_pretty(
        "min",
        grades,
        min_value(grades),
        """
        It is the smallest value in the list
        """)

    print_pretty(
        "max",
        grades,
        max_value(grades),
        """
        It is the largest value in the list
        """)

    print_pretty(
        "mean",
        grades,
        mean_value(grades),
        """
        It is the average value of all numbers in the list
        """)

    print_pretty(
        "standard deviation",
        grades,
        std_deviation_value(grades),
        """
        It is a measure, how the data is spread out around the mean.
        If the number is small, all number are spread tightly around the mean.
        If the number is large, all the number are spread out more and not so in the near of the mean value.
        """)

    print_pretty(
        "median",
        grades,
        median_value(grades),
        """
        First, the numeric list should be sorted first.
        If the list contains an odd number of entries (numbers), then the middle number is the median.
        If the list contains an even number of entries (numbers), then the two number in the middle build an average,
        that is the median.
        """)

    print_pretty(
        "median absolute deviation",
        grades,
        median_abs_dev_value(grades),
        """
        It is the deviation around the median value of the absolute difference values between the median
        and the entries of the given numbers, MAD = median(|Y_i - median(Y)|), where Y the list of the numbers.
        """)

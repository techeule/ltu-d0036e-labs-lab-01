from math import sqrt


def min_value(numerical_list):
    list_length = len(numerical_list)
    if list_length == 0:
        return None
    elif list_length == 1:
        return numerical_list[0]

    current_min_value = numerical_list[0]
    for entry in numerical_list[1:]:
        if entry < current_min_value:
            current_min_value = entry

    return current_min_value


def max_value(numerical_list):
    list_length = len(numerical_list)
    if list_length == 0:
        return None
    elif list_length == 1:
        return numerical_list[0]

    current_max_value = numerical_list[0]
    for entry in numerical_list[1:]:
        if entry > current_max_value:
            current_max_value = entry

    return current_max_value


def mean_value(numerical_list):
    list_length = len(numerical_list)
    if list_length == 0:
        return None
    elif list_length == 1:
        return numerical_list[0]

    sum_value = numerical_list[0]
    for entry in numerical_list[1:]:
        sum_value += entry

    return sum_value / list_length


def variance_value(numerical_list, around=None):
    list_length = len(numerical_list)
    if list_length == 0:
        return None
    elif list_length == 1:
        return numerical_list[0]

    around = mean_value(numerical_list) if around is None else around
    square_mean_diff_entries = [(around - x) ** 2 for x in numerical_list]
    sum_of_square_mean_diff_entries = 0
    for qmde in square_mean_diff_entries:
        sum_of_square_mean_diff_entries += qmde

    return sum_of_square_mean_diff_entries / list_length


def std_deviation_value(numerical_list):
    list_length = len(numerical_list)
    if list_length == 0:
        return None
    else:
        return sqrt(variance_value(numerical_list))


def median_value(numerical_list):
    list_length = len(numerical_list)
    if list_length == 0:
        return None
    elif list_length == 1:
        return numerical_list[0]
    elif list_length == 2:
        return (numerical_list[0] + numerical_list[1]) / 2

    numbers = [x for x in numerical_list]
    numbers.sort()

    if list_length % 2 == 1:
        return numbers[(list_length - 1) // 2]
    else:
        smallest_middle = ((list_length - 1) // 2)
        next_smallest_middle = smallest_middle + 1
        return (numbers[smallest_middle] + numbers[next_smallest_middle]) / 2


def median_abs_dev_value(numerical_list):
    list_length = len(numerical_list)
    if list_length == 0:
        return None

    median = median_value(numerical_list)
    abs_diff = [abs(x - median) for x in numerical_list]
    return median_value(abs_diff)

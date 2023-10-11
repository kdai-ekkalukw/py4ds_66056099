"""
Exercise 15
"""
import statistics

def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    if num_list != []:
        median_val = statistics.median(num_list)
    else:
        median_val = None
    return median_val

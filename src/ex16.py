"""
Exercise 16
"""
import statistics


def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    if num_list != []:
        mode_val = statistics.mode(num_list)
    else:
        mode_val = None
    return mode_val

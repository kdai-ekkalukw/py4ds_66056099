"""
Exercise 14
"""


def average(num_list) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - float: The average of the numbers in the list.
      If the list is empty, returns 0.
    """
    avg = 0
    avg = sum(num_list)/len(num_list)
    float(avg)
    return avg

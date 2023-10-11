"""
Exercise 13
"""


def calc_sum(num_list):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int: The sum of all the numbers in the list.
    """
    if num_list != []:
        sum_val = sum(num_list)
    else:
        sum_val = 0
    return sum_val


def calc_prod(num_list):
    """
    Calculates the product of all the numbers in the given list.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        int: The product of all the numbers in the list.
    """
    prod = 1
    if num_list != []:
        for i in num_list:
            prod = prod * i
    else:
        prod = 1
    return prod

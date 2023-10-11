"""
Execise 3
"""


def is_odd(num):
    """
    Check if a number is odd.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    # TODO : complete this
    ###
    if num % 2 == 0:
        bool_flag = False
    else:
        bool_flag = True
    ###
    #logic to cover scenario of decimal number.
    if num % 2 == 1:
        bool_flag = True
    else:
        bool_flag = False
    return bool_flag


def is_even(num):
    """
    Determines if a given number is even.

    Parameters:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    # TODO : complete this
    pass

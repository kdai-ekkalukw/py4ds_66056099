"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    if tsec == 0:
        return '0s'
    residual = tsec
    hr = residual // 3600 #calc hr
    residual = tsec % 3600
    m = residual // 60 #calc min
    residual = residual % 60 #final residual eq. sec

    strh = 'h'
    strm = 'm'
    strs = 's'
    strsp = ' '
    hms = ''

    if hr != 0:
        hms = str(hr) + strh + strsp
    if m != 0:
        hms = hms + str(m) + strm + strsp
    if residual != 0:
        hms = hms + str(residual) + strs
    #hms = str(hr) + strh + str(m) + strm + str(residual) + strs
    hms = hms.strip()

    return hms

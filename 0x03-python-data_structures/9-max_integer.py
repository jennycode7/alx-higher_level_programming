#!/usr/bin/python3


def max_integer(my_list=[]):
    """
    Returns the maximum value in a list of integers.
    """
    if my_list == []:
        return None
    x = my_list[0]
    for a in my_list[:]:
        if a > x:
            x = a
    return x

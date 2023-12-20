#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    returns the weighted average of all integers tuple
    """
    x = 0
    y = 0
    if my_list:
        for item in my_list:
            if type(item) is tuple:
                x += item[0] * item[1]
                y += item[1]
        return x/y
    else:
        return 0

#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Prints the first x elements of my_list.
    If x is greater than the length of my_list, prints all elements of my_list.
    """
    y = 0
    for y in range(x):
        try:
            print("{}".format(my_list[y]), end='')
            y = y + 1

        except IndexError:
            print('', end='\n')
            return y
    print('', end='\n')
    return y

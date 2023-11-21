#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the elements of a list, if the list is empty, prints x instead.

    Args:
    my_list (list): A list of integers.
    x (int): An integer.
    """
    y = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end='')
            y = y + 1
        except (TypeError, ValueError):
            y -= 1
            continue
    print("", end='\n')
    return y

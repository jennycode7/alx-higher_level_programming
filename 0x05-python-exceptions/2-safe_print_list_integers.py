#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the elements of a list, if the list is empty, prints x instead.

    Args:
    my_list (list): A list of integers.
    x (int): An integer.
    """
    y = 0
    for char in my_list[:x]:
        try:
            print("{:d}".format(char), end='')
            y = y + 1
        except (TypeError, ValueError):
            continue
    print("", end='\n')
    return y

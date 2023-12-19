#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    Prints the keys of a dictionary in lexicographic order.
    """
    for d, v in sorted(a_dictionary.items()):
        print(d, v)

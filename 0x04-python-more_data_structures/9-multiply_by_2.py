#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    Multiplies the values of a dictionary by 2.
    """
    return {k: v * 2 for k, v in a_dictionary.items()}

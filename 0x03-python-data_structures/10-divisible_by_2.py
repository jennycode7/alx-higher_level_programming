#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Returns a list of numbers that are divisible by 2
    """
    new_list = []

    for i in my_list:
        new_list += [i % 2 == 0]
    return new_list

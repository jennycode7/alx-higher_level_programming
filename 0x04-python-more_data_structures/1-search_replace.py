#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    my_list: list of ints
    search: int
    replace: int
    returns: list of ints
    """
    new_list = []

    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list

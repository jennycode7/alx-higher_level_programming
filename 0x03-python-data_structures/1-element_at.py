#!/usr/bin/python3


def element_at(my_list, idx):
    """ retrieves element at idx """
    if idx < 0 or idx >= len(my_list):
        return(None)
    for x in range(len(my_list)):
        if x == idx:
            return(my_list[x])

#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """
    deletes keys with a specific value in a dictionary.
    """
    new_dict = []
    for key,v in a_dictionary.items():
        if v == value:
            new_dict.append(key)

    for key in new_dict:
        del a_dictionary[key]
    return a_dictionary 

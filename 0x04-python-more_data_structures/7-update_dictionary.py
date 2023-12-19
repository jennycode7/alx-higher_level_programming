#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    Updates the value of a key in a dictionary.
    
    Args:
    a_dictionary (dict): a dictionary
    key (str): a key
    value (str): a value
    
    Returns:
    dict: the updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary

#!/usr/bin/python3


def best_score(a_dictionary):
    """
    Returns the key of the dictionary that has the highest value.
    """
    if a_dictionary:
        best_key = None
        best_value = 0
        for key, value in a_dictionary.items():
            if value > best_value:
                best_value = value
                best_key = key
        return best_key
    else:
        return None

#!/usr/bin/python3
"""
A module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    saves obj to filename
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
"""
A module
"""

import json


def to_json_string(my_obj):
    """
    converts my_obj to json formatted string
    """
    return json.dump(my_obj)

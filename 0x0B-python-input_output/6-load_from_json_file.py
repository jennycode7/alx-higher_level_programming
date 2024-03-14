#!/usr/bin/python3
"""
A module
"""

import json



def load_from_json_file(filename):
    """
    load from json file
    """
    with open(filename, 'r') as f:
        json_string = f.read()
        return json.loads(json_string)

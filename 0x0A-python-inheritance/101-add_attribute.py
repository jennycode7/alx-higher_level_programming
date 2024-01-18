#!/usr/bin/python3
"""
A module
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds an attribute an object
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value

    else:
        raise TypeError("can't add new attribute")

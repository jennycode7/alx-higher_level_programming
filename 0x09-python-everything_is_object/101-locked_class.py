#!/usr/bin/python3
"""
A module
"""


def LockedClass:
    """
    prevents the user from dynamically
    creating new instance attributes
    """
    __slot__ = ["first_name"]

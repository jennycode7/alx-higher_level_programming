#!/usr/bin/python3
"""
A module
"""


class LockedClass:
    """
    prevents the user from dynamically
    creating new instance attributes
    """

    __slot__ = ["first_name"]

#!/usr/bin/python3
"""
A module
"""


class Student:
    """
    A class
    """
    def __init__(self, first_name, last_name, age):
        """
        A initialializer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        To json
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

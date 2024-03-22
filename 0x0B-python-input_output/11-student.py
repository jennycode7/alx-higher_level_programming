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

    def to_json(self):
        """
        To json
        """
        return self.__dict__

    def reload_from_json(self, json):
        """
        reload to json
        """
        for attr in json:
            setattr(self, attr, json[attr])

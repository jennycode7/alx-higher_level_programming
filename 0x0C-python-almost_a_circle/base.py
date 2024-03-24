#!/usr/bin/python3
"""
A module
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize self
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

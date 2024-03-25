#!/usr/bin/python3
"""
A module
"""


class Base:
    """
    A class Base
    foundation for other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize self
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

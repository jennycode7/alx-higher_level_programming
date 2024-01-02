#!/usr/bin/python3


"""
This is an empty class
"""


class Square:
    """
    Describes a square
    """
    def __init__(self, size=0):
        """
        Initializes a size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

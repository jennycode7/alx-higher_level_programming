#!/usr/bin/python3
"""
A module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square Class
    """
    def __init__(self, size):
        """
        An initialization function
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def __str__(self):
        """
        implememt __str___
        """
        ptr = '[' + str(self.__class__.__name___) + '] '
        ptr += self.__size + '/' + self.__size
        return ptr

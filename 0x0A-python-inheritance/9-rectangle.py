#!/usr/bin/python3
"""
A module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from BaseGoemetry
    """
    def __init__(self, width, height):
        """
        initialization function
        """
        self.integer_validator("Width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Area of the rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Str Return
        """
        ptr = "[" + str(self.__class__.__name__) + "] "
        ptr += str(self.__width) + "/" + str(self.__height)
        return ptr

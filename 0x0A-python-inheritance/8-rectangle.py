#!/usr/bin/python3
"""
A module
"""
        
class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from BaseGoemetry
    """
    def __init__(self, width, height):
        """
        initialization function
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


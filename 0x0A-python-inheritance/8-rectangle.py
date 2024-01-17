#!/usr/bin/python3
"""
A module for inheritance from Base Geometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from BaseGoemetry

    BaseGeometry: another class
    """
    def __init__(self, width, height):
        """
        initialization function
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

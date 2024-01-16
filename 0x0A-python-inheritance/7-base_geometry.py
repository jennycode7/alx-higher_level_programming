#!/usr/bin/python3
"""
A Module for base goemetry
"""


class BaseGeometry:
    """
    A Class Base Goemetry
    """
    def area(self):
        """
        Area of goemetry
        """
        raise Exception('(area) is not implemented')
    def integer_validator(self, name, value):
        """
        validates an integer
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

#!/usr/bin/python3

"""
 Not an empty class
"""


class Rectangle:
    """
    A Class that defines a rectangle
    """
    def __init__(self, width, height):
        """
        sets  the width and height
        """

        self.check_width(width)
        self.check_heigth(height)

        self.width = width
        self.height = height

    @property
    def width(self):

        """
        intializes the width's value
        """

        return self.__width

    @width.setter
    def width(self, value):

        """
        width setter module
        """

        self.check_width(value)
        self.__width = value

    @property
    def height(self):
        """
        intializes the width's value
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        heigth setter module
        """

        self.check_heigth(value)
        self.__height = value

    def check_width(self, width):
        """
        checks for type of value
        then for positivity
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    def check_heigth(self, height):
        """
        checks for type of value
        then for positivity
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """
        calculates the area of the rectangle
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
        calculates the perimeter of the rectangle
        """

        return (self.__width * 2) + (self.___height * 2)

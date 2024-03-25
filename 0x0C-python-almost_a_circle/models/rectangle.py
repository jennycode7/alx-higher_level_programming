#!/usr/bin/python3
"""
A module
"""
from base import Base


class Rectangle(Base):
    """
    A class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize self
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        if not isinstance(value, int):
            raise TypeError('Width must an integer')
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        if not isinstance(value, int):
            raise TypeError('Height must an integer')
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x
    @x.setter
    def x(self, value):
        """
        Setter for x
        """
        if not isinstance(value, int):
            raise TypeError('X must an integer')
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y
    @y.setter
    def y(self, value):
        """
        Setter for y
        """
        if not isinstance(value, int):
            raise TypeError('Y must an integer')
        self.__y = value
#!/usr/bin/python3
"""
A module
"""
from models.base import Base


class Rectangle(Base):
    """
    A class Rectangle
    Inherits from base
    new attributes added
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
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
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
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
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
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
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
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        returns area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays rectangle
        """
        line = 0
        for i in range(self.height):
            while line < self.y:
                print()
                line += 1
            space = 0
            while space < self.x:
                print(' ', end='')
                space += 1
            for x in range(self.width):
                print('#', end='')
                x += 1
            print()
            i += 1

    def __str__(self):
        """
        Overrides str method
        """
        ptr = '[Rectangle]' + ' (' + str(self.id) + ')' + ' ' + str(self.x)
        ptr += '/' + str(self.y) + ' - '
        ptr += str(self.width) + '/' + str(self.height)
        return ptr

    def update(self, *args, **kwargs):
        """
        Update the rectangle
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
            if len(args) >= 6:
                raise TypeError('Too many arguments')
        else:
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

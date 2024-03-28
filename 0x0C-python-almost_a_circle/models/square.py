#!/usr/bin/python3
"""
A module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize self
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the square
        """
        ptr = '[Square]' + ' (' + str(self.id) + ')' + ' ' + str(self.x) + '/'
        ptr += str(self.y) + ' - ' + str(self.width)
        return ptr

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the rectangle
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
            if len(args) >= 5:
                raise TypeError('Too many arguments')
        else:
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

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

#!/usr/bin/python3


"""
This is an empty class
"""


class Square:
    """
    Describes a square
    """
    def __init__(self, size=0):
        """
        Initializes a size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.size = size
        self.__size = size

    @property
    def size(self):
        """
        Returns the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints the size
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2

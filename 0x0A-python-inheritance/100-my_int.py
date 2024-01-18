#!/usr/bin/python3
"""
A module
"""


class MyInt(int):
    """
    A rebel class
    """
    def __eq__(self, value):
        """
        manipulates the == operator
        """
        return not super().__eq__(value)

    def __ne__(self, value):
        """
        manipulates the != operator
        """
        return not self.__eq__(value)

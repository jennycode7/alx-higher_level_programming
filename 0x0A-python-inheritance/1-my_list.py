#!/usr/bin/python3
"""
Class mylist
"""


class MyList(list):
    """
    My Class
    """
    def print_sorted(self):
        """
        print sorted list
        """
        new = sorted(self)
        print(new)

#!/usr/bin/python3
"""
A module
"""


def print_square(size):
    """
    prints square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for x in range(size):
        for y in range(size):
            print('#', end='')
        print()

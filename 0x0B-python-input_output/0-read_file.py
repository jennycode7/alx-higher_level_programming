#!/usr/bin/python3

"""python file input and output"""

def read_file(filename=""):
    """
    Reads a file and prints its content.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')

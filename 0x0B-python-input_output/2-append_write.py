#!/usr/bin/python3
""" writes a file """


def append_write(filename="", text=""):
    """
    writes a file and prints its content.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

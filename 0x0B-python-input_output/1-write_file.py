#!/usr/bin/python3
""" writes a file """


def write_file(filename="", text=""):
    """
    writes a file and prints its content.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

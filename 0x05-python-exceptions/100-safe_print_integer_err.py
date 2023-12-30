#!/usr/bin/python3


import sys


def safe_print_integer_err(value):
    """
    Prints the integer value to stdout.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False

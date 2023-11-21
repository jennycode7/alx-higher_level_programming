#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints the given integer value.
    :param value: The integer value to print.
    :return: The number of printed characters.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

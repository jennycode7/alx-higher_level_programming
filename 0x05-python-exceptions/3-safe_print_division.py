#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Prints the division of two numbers, if b is not zero.
    """
    x = None
    try:
        x = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(x))
    return x

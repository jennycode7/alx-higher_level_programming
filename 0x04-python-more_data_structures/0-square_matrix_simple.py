#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    >>> square_matrix_simple([[1, 2], [3, 4]])
    """
    return [[x * x for x in row] for row in matrix]

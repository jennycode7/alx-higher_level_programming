#!/usr/bin/python3
"""
A module
"""

def divided_matrix(matrix, div):
    """
    divides a matrix
    """
    for row in matrix:
        x = len(row)
    
    for row in matrix:
        y = len(row)
        if not (y == x):
            raise TypeError('Each row of the matrix must have the same size')
        for i in row:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if not isinstance(div, int) and not isinstance(div, float):
            raise TypeError('div must be a number')
        if div == 0:
            raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        x = []
        for i in row:
            x.append(round(float(i / div), 2))
        new_matrix.append(x)
    return new_matrix

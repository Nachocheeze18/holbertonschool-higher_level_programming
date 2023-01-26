#!/usr/bin/python3
"""matrix function"""


def matrix_divided(matrix, div):
    """matrix divider function"""
    for row in matrix:
        if (len(row) is not (len(matrix[0]))):
            raise TypeError('Each row of the matrix must have the same size')

    if (not isinstance(div, (int, float))):
        raise TypeError('div must be a number')

    if (div == 0):
        raise ZeroDivisionError('division by zero')

    for a in matrix:
        for b in a:
            if (type(b) is not int and type(b) is not float):
                raise TypeError('matrix must be a matrix (list of lists) of'
                                ' integers/floats')

    return [[round(b/div, 2) for b in a] for a in matrix]

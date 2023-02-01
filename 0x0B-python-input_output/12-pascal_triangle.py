#!/usr/bin/python3
"""triangle file"""


def pascal_triangle(n):
    """tri function"""
    result = []
    for x in range(n):
        if x == 0:
            result.append([1])
        else:
            row = [1]
            for y in range(1, x):
                row.append(result[x-1][y-1] + result[x-1][y])
            row.append(1)
            result.append(row)
    return result

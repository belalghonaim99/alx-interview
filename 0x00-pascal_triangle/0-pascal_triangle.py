#!/usr/bin/python3
"""
Create a function def pascal_triangle(n)
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    x = []
    if n <= 0:
        return x
    x = [[1]]
    for i in range(1, n):
        y = [1]
        for j in range(len(x[i - 1]) - 1):
            y.append(x[i - 1][j] + x[i - 1][j + 1])
        y.append(1)
        x.append(y)
    return x

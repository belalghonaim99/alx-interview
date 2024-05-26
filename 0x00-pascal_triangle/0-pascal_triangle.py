#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
that returns a list of lists
Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def pascal_triangle(n):
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

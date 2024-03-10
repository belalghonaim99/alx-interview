#!/usr/bin/python3 
"""
Create a function def pascal_triangle(n):
that returns a list of lists of integers representing the Pascals triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
"""

def pascal_triangle(n):
    i = []
    if n<=0:
        return i
    i = [[1]]
    for j in range(1, n):
        i.append([1])
        for k in range(1, j):
            i[j].append(i[j-1][k-1] + i[j-1][k])
        i[j].append(1)
        return i
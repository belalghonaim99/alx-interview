#!/usr/bin/python3
""" Min Operations """


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divided = 2
    while n > 1:
        while n % divided == 0:
            operations += divided
            n //= divided
        divided += 1
    return operations

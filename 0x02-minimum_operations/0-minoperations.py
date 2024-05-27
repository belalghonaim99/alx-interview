#!/usr/bin/python3
""" Min Operations """


def minOperations(n: int) -> int:
    """ Min Operations """
    char = 'H'
    char2 = 'H'
    opeartion = 0
    while (len(char2) < n):
        if (n % len(char2) == 0):
            opeartion += 2
            char = char2
            char2 += char
    else:
        opeartion += 1
        char2 += char
    if len(char2) != n:
        return 0
    return opeartion

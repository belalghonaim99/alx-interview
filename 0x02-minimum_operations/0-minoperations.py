#!/usr/bin/python3
""" Min Operations """


def minOperations(n: int) -> int:
    """ Min Operations """
    re = 'H'
    re2 = 'H'
    opeartion = 0
    while (len(re2) < n):
        if (n % len(re2) == 0):
            opeartion += 1
            re = re2
            re2 += re2
        re2 += re
        re2 += re2
    else:
        opeartion += 1
        re2 += re
    if (len(re2) != n):
        return 0
    return opeartion

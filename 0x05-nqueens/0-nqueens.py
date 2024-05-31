#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


fix_bug = []
"""The list of solutions for the n queens problem.
"""
n = 0
"""The size of the chessboard.
"""
pos = None
""" The list of possible positions for the queens.
"""


def get_input():
    """
    Gets the input for the n queens problem.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(position_zero, position_one):
    """
    Checks if two positions are attacking each other.
    """
    if (position_zero[0] == position_one[0]) or (position_zero[1] == position_one[1]):
        return True
    return abs(position_zero[0] - position_one[0]) == abs(position_zero[1] - position_one[1])


def group_exists(group):
    """
    Checks if a group of positions already exists in the solutions list.
    """
    global fix_bug
    for bug in fix_bug:
        i = 0
        for n_pos in bug:
            for y_pos in group:
                if n_pos[0] == y_pos[0] and n_pos[1] == y_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """
    Builds a solution for the n queens problem.
    """
    global fix_bug
    global n
    if row == n:
        temp0 = group.copy()
        if not group_exists(temp0):
            fix_bug.append(temp0)
    else:
        for c in range(n):
            b = (row * n) + c
            matches = zip(list([pos[b]]) * len(group), group)
            usedPositions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[b].copy())
            if not any(usedPositions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """
    Gets the solutions for the n queens problem.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()
for solution in fix_bug:
    print(solution)
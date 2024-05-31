#!/usr/bin/python3
"""This module solves the N queens problem."""
import sys


solution = []
"""The list of solutions for the N queens problem."""
n = 0
"""The size of the chessboard."""
position = None
"""The list of possible positions for the queens."""


def get_input():
    """Validates the input arguments and returns the size of the chessboard."""
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


def is_attacking(pos0, pos1):
    """ Checks if two queens are attacking each other."""
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """Checks if a group of positions already exists in the solutions list."""
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(r, group):
    """ Builds a solution for the N queens problem."""
    global solutions
    global n
    if r == n:
        temp0 = group.copy()
        if not group_exists(temp0):
            solutions.append(temp0)
    else:
        for col in range(n):
            a = (r * n) + col
            matches = zip(list([position[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(position[a].copy())
            if not any(used_positions):
                build_solution(r + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Gets all the solutions for the N queens problem."""
    global position, n
    position = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)

#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def backtrack(board, n, colums, position, g, rows):
    """
    Backtracking function to find all possible solutions
    to the nqueens problem
    """
    if rows == n:
        response = []
        for i in range(len(board)):
            for k in range(len(board[i])):
                if board[i][k] == 1:
                    response.append([i, k])
        print(response)
        return

    for j in range(n):
        if j in colums or (rows + j) in position or (rows - j) in g:
            continue

        colums.add(j)
        position.add(rows + j)
        g.add(rows - j)
        board[rows][j] = 1

        backtrack(rows+1, n, colums, position, g, board)

        colums.remove(j)
        position.remove(rows + j)
        g.remove(rows - j)
        board[rows][j] = 0


def nqueens(n):
    """
    Function to solve the nqueens problem
    Args:
        n: int, size of the chess board
    Return:
        None
    """
    cols = set()
    pos = set()
    n_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos, n_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        g = int(n[1])
        if g < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(g)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

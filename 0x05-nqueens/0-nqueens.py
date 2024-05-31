#!/usr/bin/env python3
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    """
    Recursive utility function to solve N Queens problem
    """
    if col >= N:
        result = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    result.append([i, j])
        solutions.append(result)
        return True

    for i in range(N):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens_util(board, col + 1)

            board[i][col] = 0


def solve_nqueens(N):
    """
    Solve the N Queens problem
    """
    board = [[0] * N for _ in range(N)]
    solve_nqueens_util(board, 0)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(N)

    for sol in solutions:
        print(sol)

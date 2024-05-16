#!/usr/bin/python3
"""
N-Queens backtracking.
"""

import sys


def nqueens_helper(n, y, board):
    """
    backtracking.
    """
    for i in range(n):
        held = 0
        for j in board:
            if i == j[1] or abs(i - j[1]) == abs(y - j[0]):
                held = 1
                break
        if held == 0:
            board.append([y, i])
            if y == n - 1:
                print(board)
            else:
                nqueens_helper(n, y + 1, board)
            board.pop()


def nqueens(n):
    """
    Solve the N-Queens n x n.
    """
    board = []
    nqueens_helper(n, 0, board)


def main():
    """
    Main function.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(n)


if __name__ == "__main__":
    main()

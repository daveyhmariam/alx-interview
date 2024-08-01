#!/usr/bin/python3
"""
N Queens problem: placing N non-attacking queens on an N×N chessboard
using backtracking algorithm
"""

skew_right = set()
skew_left = set()
rows = set()
solution = []
methods = []

def nqueens(N, column):
    """Recursive function with backtracking algorithm for N queens problem

    Args:
        N (int): board size
        column (int): current column
    """
    if column >= N:
        methods.append(solution.copy())
        return

    for row in range(N):
        if (row not in rows and 
            row + column not in skew_left and
            row - column not in skew_right):
            rows.add(row)
            skew_left.add(row + column)
            skew_right.add(row - column)
            solution.append([row, column])
            nqueens(N, column + 1)
            rows.remove(row)
            skew_right.remove(row - column)
            skew_left.remove(row + column)
            solution.remove([row, column])

if __name__ == "__main__":
    """
    Execute N Queens solution
    """
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        board = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(board, 0)
    for item in methods:
        print(item)

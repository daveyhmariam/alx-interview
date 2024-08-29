#!/usr/bin/python3
"""
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid:
"""


def island_perimeter(grid):
    """Return theperimeter of an Island

    Args:
        grid (int):
    """
    p = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                p += 4

                if i > 0 and grid[i-1][j] == 1:
                    p -= 2

                # Check left (i, j-1)
                if j > 0 and grid[i][j-1] == 1:
                    p -= 2

    return p

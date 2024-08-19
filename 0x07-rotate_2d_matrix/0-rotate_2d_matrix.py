#!/usr/bin/python3
"""
List comprehnsions 2D matrix rotation
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees

    Args:
    matrix : n x n matrix

    Returns:
    None: matrix modified in place.
    """
    matrix[:] = [[row[i] for row in matrix] for i in range(len(matrix))]
    matrix[:] = [row[::-1] for row in matrix]
    return matrix

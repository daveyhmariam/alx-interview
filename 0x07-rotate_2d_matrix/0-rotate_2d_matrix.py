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
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

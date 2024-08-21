#!/usr/bin/python3
"""
pascal triangle interview question
"""
from typing import List


def pascal_triangle(n) -> List[List[int]]:
    """Pascal triangle list of lists
    formula nCm = n-1Cm-1 + n-1Cm

    Args:
        n (int):level of pascal triangle
    """
    if n <= 0:
        return []
    pascal = [[1]]
    for i in range(1, n):
        pascal_row = [1]
        for j in range(1, i):
            pascal_row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal_row.append(1)
        pascal.append(pascal_row)
    return pascal

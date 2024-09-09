#!/usr/bin/python3
"""
minOperations function.
"""


def minOperations(n: int) -> int:
    """
    In a text file, there is a single character H.
    Thetext editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, the method calculates
    the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations
        required to achieve n 'H' characters.
        n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0
    operation = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operation += factor
            n //= factor
        factor += 1
    return operation

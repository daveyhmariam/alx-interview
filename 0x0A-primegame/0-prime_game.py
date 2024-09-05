#!/usr/bin/python3
"""
Sieve of Eratosthenes Algorithm
"""


def isWinner(x, nums):
    """

    Args:
        x (int): Number of rounds
        nums (array): Contains ranges on which the game is played on

    Return (str): The name of the player won the most
    """
    for i in nums:
        p = findPrime(i)
        x -= len(p) % 2
    if x < len(nums) // 2:
        return "Maria"
    return 'Ben'


def findPrime(n):
    """Returns prime numbers upto n

    Args:
        n (int): The range to find primes within
    """
    n += 1
    arr = [True] * n
    primes = []
    for i in range(2, n):
        if arr[i]:
            primes.append(i)
            if i * i < n:
                for j in range(i * i, n, i):
                    arr[j] = False
    return primes

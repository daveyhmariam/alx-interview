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
    b = 0
    m = 0
    for i in nums:
        p = findPrime(i)
        if len(p) % 2 == 1:
            m += 1
        else:
            b += 1
    print(m, b)
    if m > b:
        return "Maria"
    if m < b:
        return 'Ben'
    else:
        None

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

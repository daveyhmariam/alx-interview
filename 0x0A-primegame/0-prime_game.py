#!/usr/bin/python3
"""
Sieve of Eratosthenes Algorithm
"""


def isWinner(x, nums):
    """
    Determines the winner of a game based on prime numbers within given ranges.

    Args:
        x (int): Number of rounds played.
        nums (list): List of ranges (integers) on which the game is played.

    Returns:
        str: The name of the winning player ("Maria" or "Ben"),
        or None if there's a tie.
    """

    if x == 0 or not nums:
        return None  # Handle empty input or zero rounds

    maria_wins = 0
    ben_wins = 0

    for i in nums:
        prime_count = find_primes(i)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None


def find_primes(n):
    """
    Finds the number of prime numbers up to a given
    limit using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit for finding primes.

    Returns:
        int: The count of prime numbers found.
    """

    n += 1  # Include the limit itself
    primes = [True] * n
    primes[0] = primes[1] = False  # Mark 0 and 1 as non-prime

    for i in range(2, int(n**0.5) + 1):  # Optimize iteration limit
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    return sum(primes)  # Count the remaining True values

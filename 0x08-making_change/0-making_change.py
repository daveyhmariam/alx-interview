#!/usr/bin/python3
"""
Making change with given number of coins
with the list number of coins
"""

def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.

    Args:
        coins (List[int]): List of coin denominations
        total (int): The total amount of change

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if not possible
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Try to use the fewest number of coins
    num_coins = 0
    remaining_amount = total

    for coin in coins:
        if remaining_amount == 0:
            break
        num_coins += remaining_amount // coin
        remaining_amount %= coin

    # If we could not make the exact amount, return -1
    return num_coins if remaining_amount == 0 else -1

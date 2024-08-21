#!/usr/bin/python3
"""
Making change with given number of coins
with the list number of coins
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total

    Args:
        coins (List): list of coin denomination
        total (int): the total amount of change
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    for i in range(len(coins)):
        c = coins[i:]
        sum = 0
        mod = total
        for elm in c:
            sum += (mod // elm)
            mod %= elm
            if mod == 0:
                return sum
    return -1

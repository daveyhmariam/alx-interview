# 0x08. Making Change

## Overview

This project tackles the classic coin change problem, a common problem in the domain of dynamic programming and greedy algorithms. The goal is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. This project challenges you to devise a solution that is both correct and efficient.

## Project Details

- **Algorithm**: Dynamic Programming and Greedy Algorithms
- **Programming Language**: Python
- **Weight**: 1
- **Start Date**: August 19, 2024, 6:00 AM
- **End Date**: August 23, 2024, 6:00 AM
- **Checker Release Date**: August 20, 2024, 6:00 AM
- **Auto Review**: An automatic review will be conducted at the deadline.

## Key Concepts

### Greedy Algorithms
- Understanding the concept and application of greedy algorithms for the coin change problem.
- Recognizing when greedy algorithms may not provide an optimal solution.

### Dynamic Programming
- Basic principles and application of dynamic programming.
- Handling overlapping subproblems and optimal substructure.

### Algorithmic Complexity
- Analyzing the time and space complexity of your solutions.
- Aiming for efficient solutions that meet runtime constraints.

### Problem-Solving Strategies
- Breaking down the problem into smaller, manageable sub-problems.
- Choosing between iterative and recursive approaches.

### Python Programming
- Manipulating lists and utilizing list comprehensions.
- Implementing efficient functions with looping and conditional statements.

## Resources

### Python Official Documentation
- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)

### GeeksforGeeks Articles
- [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
- [Greedy Algorithm to Find Minimum Number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

### YouTube Tutorials
- [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=9Ier1B_Vjz8)

## Requirements

- **Allowed Editors**: vi, vim, emacs
- **Interpreter**: Ubuntu 20.04 LTS with Python 3 (version 3.4.3)
- **File Requirements**:
  - All files must end with a new line.
  - The first line of all files should be `#!/usr/bin/python3`.
  - A `README.md` file is mandatory.
  - Code should follow PEP 8 style (version 1.7.x).
  - All files must be executable.

## Tasks

### 0. Change Comes from Within
- **Prototype**: `def makeChange(coins, total):`
- **Description**: Given a pile of coins of different values, determine the fewest number of coins needed to meet a given total amount.
  - **Parameters**:
    - `coins`: List of integers representing the values of coins.
    - `total`: Integer representing the amount to be made.
  - **Return**:
    - The fewest number of coins needed to meet the total.
    - If `total` is 0 or less, return 0.
    - If `total` cannot be met with the given coins, return -1.

### Example Usage

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

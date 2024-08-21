# 0x00. Pascal's Triangle

## Overview
This project involves implementing a Python function that generates Pascal's Triangle. Pascal's Triangle is a triangular array of binomial coefficients, where each number is the sum of the two directly above it.

### Learning Objectives
By completing this project, you will:
- Understand how to manipulate lists and list comprehensions in Python.
- Apply loops, conditional statements, and arithmetic operations to solve problems.
- Develop a function that returns a list of lists representing Pascal's Triangle.
- Optionally, explore recursion and memory management concepts.

## Resources
- [What is Pascal’s Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?v=XMriWTvPXHI)
- [Python Algorithms](https://www.geeksforgeeks.org/algorithms-in-python/)

## Project Details

### Task: Pascal's Triangle
#### Requirements:
- Create a function `def pascal_triangle(n):` that returns a list of lists representing the Pascal’s Triangle of `n`.
- The function should return an empty list if `n <= 0`.

#### Example:
```python
~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))



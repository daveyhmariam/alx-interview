# 0x09. Island Perimeter

## Algorithm | Python

### Project Overview

This project focuses on solving a geometric problem within a grid context, specifically calculating the perimeter of a single island in a grid. The grid is represented by a 2D array of integers, where:
- `0` represents water
- `1` represents land

You will need to apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to achieve the goal.

### Concepts Needed

#### 1. 2D Arrays (Matrices)
- **Accessing and Iterating**: Learn how to navigate through the elements of a 2D array.
- **Adjacent Cells**: Understand how to move horizontally and vertically between cells.

#### 2. Conditional Logic
- **Cell Contribution**: Apply conditions to determine whether a cell contributes to the perimeter of the island.

#### 3. Counting Techniques
- **Edge Counting**: Develop a method to count the edges that contribute to the island’s perimeter.

#### 4. Problem-Solving Strategies
- **Breaking Down the Problem**: Identify land cells and calculate their contribution to the perimeter.

#### 5. Python Programming
- **Nested Loops**: Use nested loops to iterate over grid cells.
- **Conditional Statements**: Check the status of adjacent cells.

### Resources

#### Python Official Documentation
- **Nested Lists**: Understanding how to work with lists within lists in Python.

#### GeeksforGeeks Articles
- **Python Multi-dimensional Arrays**: A guide to working with 2D arrays in Python effectively.

#### TutorialsPoint
- **Python Lists**: Explains how to create, access, and manipulate lists in Python.

#### YouTube Tutorials
- **Python 2D arrays and lists**

### Requirements

- **Allowed editors**: vi, vim, emacs
- **Interpreter/Compiler**: Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Endings**: All files should end with a new line
- **First Line**: The first line of all your files should be exactly `#!/usr/bin/python3`
- **README.md**: A README.md file at the root of the folder is mandatory
- **Style**: Follow PEP 8 style (version 1.7)
- **Modules**: No module imports allowed
- **Documentation**: All modules and functions must be documented
- **Executables**: All files must be executable

### Tasks

#### 0. Island Perimeter

**Objective**: Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`.

- **Grid Description**:
  - `grid` is a list of list of integers.
  - `0` represents water.
  - `1` represents land.
  - Each cell is square, with a side length of 1.
  - Cells are connected horizontally/vertically (not diagonally).
  - The grid is rectangular, with width and height not exceeding 100.
  - The grid is completely surrounded by water.
  - There is only one island (or none).
  - The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

**Example:**

```python
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

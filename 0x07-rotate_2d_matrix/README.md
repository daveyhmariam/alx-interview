# 0x07. Rotate 2D Matrix

## Algorithm | Python  
**Weight:** 1  
**Project Start:** Aug 12, 2024 6:00 AM  
**Project End:** Aug 16, 2024 6:00 AM  
**Checker Release:** Aug 13, 2024 6:00 AM  
**Auto Review:** Launched at the deadline  

---

## Description

For this project, you are tasked with implementing an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. This challenge requires proficiency in matrix manipulation and in-place operations in Python. The solution involves matrix transposition followed by reversing rows.

---

## Key Concepts

### 1. Matrix Representation in Python:
- Understanding how 2D matrices are represented using lists of lists in Python.
- Accessing and modifying elements in a 2D matrix.

### 2. In-place Operations:
- Perform operations directly on the data without creating a copy of the data structure.
- Minimize space complexity by modifying the matrix in place.

### 3. Matrix Transposition:
- Transposing a matrix involves swapping rows with columns.
- Transposition is a key step in the rotation process.

### 4. Reversing Rows:
- After transposing, rows of the matrix are reversed to achieve the final 90-degree rotation.

### 5. Nested Loops:
- Use of nested loops to iterate through the matrix and manipulate its elements for rotation.

---

## Resources

### Python Documentation:
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html) (List comprehensions, nested lists)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### GeeksforGeeks Articles:
- [In-place rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### TutorialsPoint:
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm) for basics of list manipulation in Python.

---



## Task

### 0. Rotate 2D Matrix (Mandatory)
Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.

**Prototype**:  
```python
def rotate_2d_matrix(matrix):

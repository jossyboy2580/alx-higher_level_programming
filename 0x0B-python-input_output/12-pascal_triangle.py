#!/usr/bin/python3
"""
This module contains a function that returns the pascal
triangle
"""


def pascal_triangle(n):
    """
    A function that returns a pascal trangle
    """
    triangle = []
    for i in range(n):
        entry = []
        for j in range(i+1):
            if j == 0 or j == i:
                entry.append(1)
            else:
                entry.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(entry)
    return triangle

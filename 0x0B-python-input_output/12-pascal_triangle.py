#!/usr/bin/python3
"""
This module contains a function that returns the pascal
triangle
"""


def pascal_triangle(n):
    """
    A function that returns a pascal trangle
    """
    pascal = list()
    if n:
        for i in range(1, n):
            pascal.append([j for j in range(1, i)])

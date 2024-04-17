#!/usr/bin/python3
"""
A module containing a file opening function
"""


def read_file(filename=""):
    if filename:
        with open(filename, encoding='utf-8') as fp:
            line = fp.readline()
            print(line)

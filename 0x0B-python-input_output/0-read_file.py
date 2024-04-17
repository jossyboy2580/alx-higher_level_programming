#!/usr/bin/python3
"""
A module containing a file opening function
"""


def read_file(filename=""):
    """ A function to reaf files """
    if filename:
        with open(filename, 'r', encoding='utf-8') as fp:
            line = fp.readline()
            while line:
                print(line.rstrip())
                line = fp.readline()

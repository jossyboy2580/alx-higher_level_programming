#!/usr/bin/python3
"""
A module containing a function that appends a line
to a file after the presence of a paticular string
in that file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function searches foe 'search_string'
    in filename and replaces it with 'new_string'
    """

    with open(filename, 'rw') as fi_w:

#!/usr/bin/python3
"""
A file i/o module for appending to a file
"""


def append_write(filename="", text=""):
    """
    This function opens a file for appending texts
    """
    if filename and text:
        with open(filename, 'a', encoding='utf-8') as fp:
            prev_pos = fp.tell()
            fp.write(text)
            new_pos = fp.tell()
            fp.close()
            return (new_pos - prev_pos)

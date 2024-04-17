#!/usr/bin/python3
"""
A module for writing into a file
"""


def write_file(filename="", text=""):
    """ This function writes into a file """
    if filename and text:
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write(text)
            char_count = fp.tell()
            fp.close()
            return (char_count)

#!/usr/bin/python3
"""
A module that opens a file and writes a jsonified
python object into it
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function to save a python object into a json file
    """
    if filename:
        with open(filename, 'w', encoding='utf-8') as fp:
            jsonic = json.dumps(my_obj)
            fp.write(jsonic)
            fp.close()

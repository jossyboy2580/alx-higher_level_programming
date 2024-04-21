#!/usr/bin/python3
"""
Load a json file and extract it's content
"""
import json


def load_from_json_file(filename):
    """
    A json file loading function
    """
    if filename:
        with open(filename, 'r', encoding='utf-8') as fp:
            jsonic = fp.read()
            to_str = json.loads(jsonic)
            fp.close()
            return (to_str)

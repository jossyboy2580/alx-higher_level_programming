#!/usr/bin/python3
"""
A module containing a JSON loader
"""
import json


def from_json_string(my_str):
    """ A function that loads JSON files """
    return (json.loads(my_str))

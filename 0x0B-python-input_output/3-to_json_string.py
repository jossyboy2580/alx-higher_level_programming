#!/usr/bin/python3
"""
A json serializer for python objects
"""
import json


def to_json_string(my_obj):
    """ This function prints the json form of a
    python object
    """
    return (json.dumps(my_obj))

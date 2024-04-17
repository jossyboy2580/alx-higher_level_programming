#!/usr/bin/python3
import json
"""
A json serializer for python objects
"""


def to_json_string(my_obj):
    """ This function prints the json form of a
    python object
    """
    if my_obj:
        return (json.dumps(my_obj))

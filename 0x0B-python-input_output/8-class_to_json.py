#!/usr/bin/python3
"""
Module for preparing objects for JSON ops
"""


def class_to_json(obj):
    """
    Convert an object to a serializable form
    """
    if obj:
        attrs = vars(obj)
        return (attrs)

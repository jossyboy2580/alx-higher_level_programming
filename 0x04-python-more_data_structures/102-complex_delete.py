#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary and value:
        deletion_key = None
        for key in a_dictionary:
            if a_dictionary[key] is value:
                deletion_key = key
                break
        if deletion_key:
            del (a_dictionary[deletion_key])

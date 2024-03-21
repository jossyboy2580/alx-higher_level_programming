#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    highest_value = -1000000000000000
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > highest_value:
                best_key = key
                highest_value = value
    return (best_key)

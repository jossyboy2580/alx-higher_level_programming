#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        keys_list = sorted(list(a_dictionary.keys()))
        for key in keys_list:
            print("{}: {}".format(key, a_dictionary[key]))

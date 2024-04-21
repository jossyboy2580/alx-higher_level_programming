#!/usr/bin/python3
"""
A script to add all arguments to a list
"""
import json
import sys


def main():
    """
    The main function of a program to make a json file
    from command line args
    """
    filename = "add_item.json"
    load_from_json = __import__("6-load_from_json_file").load_from_json_file
    try:
        arg_list = load_from_json(filename)
    except FileNotFoundError:
        arg_list = list()
    i = 1
    while (len(sys.argv) > i):
        arg_list.append(sys.argv[i])
        i += 1
    save_json_2_fp = __import__("5-save_to_json_file").save_to_json_file
    save_json_2_fp(arg_list, filename)


if __name__ == "__main__":
    main()

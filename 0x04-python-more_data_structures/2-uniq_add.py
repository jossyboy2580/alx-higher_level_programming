#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    if my_list:
        uniqued = set(my_list)
        for item in uniqued:
            result += item
    return (result)

#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return (None)
    new_max = -100000000000
    for value in my_list:
        if value > new_max:
            new_max = value
    return (new_max)

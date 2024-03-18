#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for i in range(2):
        elem1 = 0
        elem2 = 0
        if i <= len(tuple_a) - 1:
            elem1 = tuple_a[i]
        if i <= len(tuple_b) - 1:
            elem2 = tuple_b[i]
        new_tuple = new_tuple + ((elem1 + elem2),)
    return (new_tuple)

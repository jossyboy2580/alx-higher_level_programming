#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    if len(tuple_a) > len(tuple_b):
        max_len = len(tuple_a)
    else:
        max_len = len(tuple_b)
    for i in range(max_len):
        elem1 = 0
        elem2 = 0
        if i <= len(tuple_a):
            elem1 = tuple_a[i]
        if i <= len(tuple_b):
            elem2 = tuple_b[i]
        new_tuple = new_tuple , (elem1 + elem2)
    return (new_tuple)

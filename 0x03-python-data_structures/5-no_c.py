#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        listy = [c for c in my_string if c != "c" and c != "C"]
        return ("".join(listy))
    return ("")

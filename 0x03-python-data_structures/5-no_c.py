#!/usr/bin/python3
def no_c(my_string):
    listy = list(my_string)
    len_listy = len(listy)
    for i in range(len_listy):
        if listy[i] == "c" or listy[i] == "C":
            listy.pop(i)
    return ("".join(listy))

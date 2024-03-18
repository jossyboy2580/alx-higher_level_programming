#!/usr/bin/python3
def no_c(my_string):
    listy = list(my_string)
    for i in listy:
        if i == "c" or i == "C":
            listy.remove(i)
    return ("".join(listy))

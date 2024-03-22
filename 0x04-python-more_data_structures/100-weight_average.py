#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    weight = 0
    for item in my_list:
        total += item[0] * item[1]
        weight += item[1]
    return (total / weight)

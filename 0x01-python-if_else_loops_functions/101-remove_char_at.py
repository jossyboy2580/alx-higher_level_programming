#!/usr/bin/python3
def remove_char_at(strn, n):
    if strn:
        str_list = list(strn)
        if len(str_list) > n and n > 0:
            str_list.pop(n)
        return ("{:s}".format("".join(str_list)))

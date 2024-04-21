#!/usr/bin/python3
magic_string():
    magic_string.counter += 1
    return (("BestSchool, " * magic_string.counter).strip(", "))
magic_string.counter = 0

#!/usr/bin/python3
for c in "abcdefghijklmnopqrstuvwxyz":
    if c == "q" or c == "e":
        continue
    print("{}".format(c), end="", sep="")

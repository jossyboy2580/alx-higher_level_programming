#!/usr/bin/python3
def alphab_reversed():
    for letter in "zyxwvutsrqponmlkjihgfedcba":
        if ord(letter) % 2 != 0:
            print("{:s}".format(chr(ord(letter) - 32)), end="")
        else:
            print("{:s}".format(letter), end="")


if __name__ == "__main__":
    alphab_reversed()

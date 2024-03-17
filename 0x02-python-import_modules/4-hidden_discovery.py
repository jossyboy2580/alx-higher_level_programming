#!/usr/bin/python3
import hidden_4


def display():
    hidden = dir(hidden_4)

    for name in hidden:
        if name[0] != "_":
            print("{:s}".format(name))


if __name__ == "__main__":
    display()

#!/usr/bin/python3
import sys


def infinite_adder():

    args_count = len(sys.argv) - 1
    total = 0

    for i in range(args_count):
        total += int(sys.argv[i + 1])
    print("{:d}".format(total))


if __name__ == "__main__":
    infinite_adder()

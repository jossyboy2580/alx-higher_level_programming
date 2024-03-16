#!/usr/bin/python3
import sys


def argzz():

    args_count = len(sys.argv) - 1
    arg_message = "argument"
    arg_prefix = "."
    if args_count > 1 or args_count == 0:
        arg_message = "arguments"
        arg_prefix = ":"
    print("{} {}{}".format(args_count, arg_message, arg_prefix))
    if args_count > 0:
        for i in range(args_count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))


if __name__ == "__main__":
    argzz()

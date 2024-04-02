#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as exc:
        status = False
        sys.stderr.write("Exception: ".format(exc))
    else:
        status = True
    return (status)

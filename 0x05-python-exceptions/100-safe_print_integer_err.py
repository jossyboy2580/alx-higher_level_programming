#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as exc:
        status = False
        print("Exception: {}".format(exc), file=sys.stderr)
    else:
        status = True
    finally:
        return (status)

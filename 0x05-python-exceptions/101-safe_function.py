#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        print("{}".format(result))
    except Exception as exc:
        result = None
        print("Exception: {}".format(exc), file=sys.stderr)
    finally:
        return (result)

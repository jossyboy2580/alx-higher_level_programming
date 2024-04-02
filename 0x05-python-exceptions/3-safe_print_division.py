#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = a / b
    except ZeroDivisionError:
        status = None
    else:
        print("Inside result: {}".format(quotient))
        status = quotient
    finally:
        return (status)

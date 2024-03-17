#!/usr/bin/python3
import calculator_1
import sys


def calc():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operations = dir(calculator_1)
    allowed_operators = "+-*/"
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator not in allowed_operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if operator == "+":
        result = calculator_1.add(a, b)
    if operator == "-":
        result = calculator_1.sub(a, b)
    if operator == "*":
        result = calculator_1.mul(a, b)
    if operator == "/":
        result = calculator_1.div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    calc()

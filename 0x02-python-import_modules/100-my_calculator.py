#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) <= 3:
        print("{} <a> <operator> <b>".format(argv[0]))
        exit(1)

    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print("Unkown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))

#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        val = number % 10
    elif number < 0:
        val = -number % 10
    elif number == 0:
        val = 0
    print("{}".format(val), end='')
    return val

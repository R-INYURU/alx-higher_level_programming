#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    rem = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            rem += 1
        except IndexError:
            break
    print("")
    return (rem)

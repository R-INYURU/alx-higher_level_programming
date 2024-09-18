#!/usr/bin/python3
def print_sorted_dictionary(a_dict):
    for i in sorted(a_dict):
        print("{}: {}".format(i, a_dict[i]))

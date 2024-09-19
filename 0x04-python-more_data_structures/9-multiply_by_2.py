#!/usr/bin/python3
def multiply_by_2(a_dict):
    new_dict = {}
    this_lst = list(sorted(a_dict))
    for i in this_lst:
        new_dict[i] = a_dict[i] * 2
    return (new_dict)

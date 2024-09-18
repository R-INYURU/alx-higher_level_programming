#!/usr/bin/python3
def uniq_add(my_list=[]):
    this_set = set(my_list)
    rslt = 0
    for i in this_set:
        rslt += i
    return (rslt)

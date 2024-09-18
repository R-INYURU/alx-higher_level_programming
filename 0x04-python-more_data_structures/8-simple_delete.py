#!/usr/bin/python3
def simple_delete(a_dict, key=''):
    if key not in a_dict:
        return (a_dict)
    else:
        del a_dict[key]
    return (a_dict)

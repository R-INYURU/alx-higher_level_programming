#!/usr/bin/python3
def best_score(a_dict):
    max = 0
    key = ""
    try:
        for i in sorted(a_dict):
            if a_dict[i] > max:
                max = a_dict[i]
                key = i
            else:
                key = i
        return (key)
    except TypeError:
        return ("None")

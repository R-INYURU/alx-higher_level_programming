#!/usr/bin/python3
def remove_char_at(str, n):
    strg = ''
    for i in range(len(str)):
        if i == n:
            continue
        else:
            strg += str[i]
    return strg

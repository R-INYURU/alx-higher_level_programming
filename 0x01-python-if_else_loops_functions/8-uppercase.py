#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        val = ord(ch)
        print("{}".format(chr(val-32) if val > 96 and val < 123 else chr(val)))

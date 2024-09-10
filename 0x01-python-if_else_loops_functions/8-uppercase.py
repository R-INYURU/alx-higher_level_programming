#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        val = ord(ch)
        if val > 96 and val < 123:
            wrt = 1
        else:
            wrt = 0
        print("{}".format(chr(val-32) if wrt == 1 else chr(val)), end='')
    print()

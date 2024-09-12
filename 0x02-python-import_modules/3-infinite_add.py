#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0")
    else:
        num = 0
        for i in range(len(argv) - 1):
            num += int(argv[i + 1])
        print("{}".format(num))

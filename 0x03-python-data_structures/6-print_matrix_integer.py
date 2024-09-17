#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for (k, j) in enumerate(i):
            num = "{:d}"
            if k == (len(i) - 1):
                print(num.format(j), end='')
            else:
                print(num.format(j), end=' ')
        print()

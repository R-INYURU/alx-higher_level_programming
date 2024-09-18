#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtrx = []
    for i in matrix:
        mtrx = list(map(lambda x: x**2, i))
    return (mtrx)

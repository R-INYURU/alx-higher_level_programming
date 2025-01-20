#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices
"""


def matrix_mul(mtx_a, mtx_b):
    """ Function that multiplies 2 matrices
    Args:
       mtx_a: matrix a
       mtx_b: matrix b
    Returns:
       product
    Raise:
       TypeError:
           - if mtx_a or mtx_b aren't list,
           - if mtx_a or mtx_b aren't a list of a lists
           - if the lists of mtx_a or mtx_b don't have integers of floats
           - if the rows of mtx_a or mtx_b don't have the same size
       ValueError:
           - if mtx_a or mtx_b are empty
           - if mtx_a and mtx_b can't be multiplied
    """

    if not isinstance(mtx_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(mtx_b, list):
        raise TypeError("m_b must be a list")

    for item in mtx_a:
        if not isinstance(item, list):
            raise TypeError("m_a must be a list of lists")

    for item in mtx_b:
        if not isinstance(item, list):
            raise TypeError("m_b must be a list of lists")

    if len(mtx_a) == 0 or (len(mtx_a) == 1 and len(mtx_a[0]) == 0):
        raise ValueError("mtx_a can't be empty")

    if len(mtx_b) == 0 or (len(mtx_b) == 1 and len(mtx_a[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in mtx_a:
        for item in lists:
            if not type(item) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in mtx_b:
        for item in lists:
            if not type(item) in (int, float):
                raise TypeError("m_b should contain only integers of floats")

    length = 0

    for item in mtx_a:
        if length != 0 and length != len(item):
            raise TypeError("each row of m_a must be of the same size")
        length = len(item)

    length = 0

    for item in mtx_b:
        if length != 0 and length != len(item):
            raise TypeError("each row of m_b must be of the same size")
        length = len(item)

    if len(mtx_a[0]) != len(mtx_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r1 = []
    i1 = 0

    for a in mtx_a:
        r2 = []
        i2 = 0
        num = 0
        while (i2 < len(mtx_b[0])):
            num += a[i1] * mtx_b[i1][i2]
            if i1 == len(mtx_b) - 1:
                i1 = 0
                i2 += 1
                r2.append(num)
                num = 0
            else:
                i1 += 1
        r1.append(r2)

    return (r1)

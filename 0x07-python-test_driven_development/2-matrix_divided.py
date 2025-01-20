#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix
    Args:
       matrix: list of a lists of integers/floats
       div: number which divides tha matrix
    Returns:
       Matrix of the product
    Raise:
       TypeError:
           - If the elements of the matrix aren't lists
           - If the elements of the lists aren't integers/floats
           - If div is not an integer/float
           - If the lists of the matrix don't have the same size
      ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for item in matrix:
        if not item or not isinstance(item, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(item) != len_e:
            raise TypeError(msg_size)

        for num in item:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        len_e = len(item)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)

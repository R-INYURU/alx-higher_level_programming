#!/usr/bin/python3
"""
Use 'NumPy' and create a function multipling 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices using NumPy
    Args:
        m_a: matrix a
        m_b: matrix b
    Return:
        multiplication product
    """

    return (np.matmul(m_a, m_b))

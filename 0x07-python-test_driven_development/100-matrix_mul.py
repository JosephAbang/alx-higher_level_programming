#!/usr/bin/python3
"""Module contains functions"""


def matrix_mul(m_a, m_b):
    """
    function that performs Matrix multiplication - only
    Matrix product (two matrices)"""
    if not m_a or not m_b:
        return []

    if len(m_a[0]) != len(m_b):
        raise ValueError("Incompatible matrix dimensions for multiplication")
    new_matrix = []
    i = 0
    for lst in range(len(m_a)):
        new_list = []
        for m in range(len(m_a[0])):
            res = 0
            for n in range(len(m_b)):
                res += m_a[lst][n] * m_b[n][m]
            new_list.append(res)
        new_matrix.append(new_list)

    return new_matrix

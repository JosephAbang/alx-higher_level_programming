#!/usr/bin/python3
"""Module contains functions"""


def matrix_mul(m_a, m_b):
    """
    function that performs Matrix multiplication - only
    Matrix product (two matrices)
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    elif not isinstance(m_b, list):
        raise TypeError("m_a must be a list")

    elif not m_a:
        raise ValueError("m_a can't be empty")
    
    elif not m_b:
        raise ValueError("m_b can't be empty")

    elif not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a should contain only lists")

    elif not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b should contain only lists")

    elif len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must have the same size")

    elif len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must have the same size")

    elif len(m_a[0]) != len(m_b):
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

#!/usr/bin/python3
"""Module divides a matrix using another number"""


def matrix_divided(matrix, div):
    """Function divides all elements of a matrix"""

    if matrix is None or len(matrix) == 0:
        return [[]]
    list_len = len(matrix[0])
    for mat_list in matrix:
        for num in mat_list:
            if type(num) not in [int, float]:
                raise TypeError("matrix must \
be a matrix (list of lists) of integers/floats")
        if len(mat_list) == list_len:
            continue
        else:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_mat = []
        i = 0
        for mat_list in matrix:
            new_list = []
            for num in mat_list:
                new_list.append(round((num / div), 2))
            new_mat.append(new_list)
    return new_mat

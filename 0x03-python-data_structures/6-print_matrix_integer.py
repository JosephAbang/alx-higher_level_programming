#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for _list in matrix:
        for elem in _list:
            if _list.index(elem) < (len(_list) - 1):
                print('{:d}'.format(elem), end=' ')
            else:
                print('{:d}'.format(elem), end='')
        print()

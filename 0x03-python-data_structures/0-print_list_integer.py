#!/usr/bin/python3
def print_list_integer(my_list=[]):
    print_list = list(map(lambda x: print("{:d}".format(x)), my_list))
    return print_list

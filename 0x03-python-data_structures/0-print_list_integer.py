#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # for item in my_list:
        # print('{}'.format(item))
    print_list = list(map(lambda x: print("{:d}".format(x)), my_list))
    return print_list

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

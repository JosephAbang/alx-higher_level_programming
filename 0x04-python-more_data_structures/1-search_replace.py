#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search not in my_list:
        return my_list
    new_list = my_list[:]
    for x in my_list:
        if x == search:
            new_list[new_list.index(x)] = replace
    return new_list

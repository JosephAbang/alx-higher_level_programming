#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    temp_dict = dict(a_dictionary)
    for k in temp_dict.keys():
        if k == key:
            del a_dictionary[key]
    return a_dictionary

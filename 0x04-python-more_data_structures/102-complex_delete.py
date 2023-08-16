#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_clone = dict(a_dictionary)
    for key, val in dict_clone.items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary

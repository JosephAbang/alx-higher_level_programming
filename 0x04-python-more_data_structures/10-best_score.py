#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = 0
    max_key = ''
    for key, value in a_dictionary.items():
        if value < 0 and max_value > value:
            max_key, max_value = key, value
        elif value > max_value:
            max_key, max_value = key, value
    return (max_key)

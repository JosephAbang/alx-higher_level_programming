#!/usr/bin/python3
"""Module contains serialization function"""


def class_to_json(obj):
    """
    function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """

    if not isinstance(obj, object):
        raise ValueError("Input is not an instance of a class")

    serial_data = vars(obj)
    return serial_data

#!/usr/bin/python3
"""
module contains function that writes to and saves a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        data = json.dumps(my_obj)
        f.write(data)

#!/usr/bin/python3
"""
module contains function that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'"""

    with open(filename, mode="r", encoding="utf-8") as my_file:
        data = my_file.read()
        my_obj = json.loads(data)
        return my_obj

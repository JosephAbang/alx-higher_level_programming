#!/usr/bin/python3
"""
module contains function that returns the object representation of a JSON
"""
import json


def from_json_string(my_str):
    """
    a function that returns an object (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)

#!/usr/bin/python3
"""Module contains a class"""


class Student():
    """creates instances of student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            attr_dict = {}
            for item in attrs:
                if item in vars(self).keys():
                    attr_dict[item] = vars(self)[item]
            return attr_dict
        else:
            return vars(self)

    def reload_from_json(self, json):
        new_json = vars(self)
        updated = {}
        for key in json.keys():
            updated[key] = new_json[key]
        return updated

#!/usr/bin/python3
"""Module contains a class named BAse"""
import json


class Base:
    """base of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize instance attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert json to string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            json_list = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """convert json to string"""
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create an instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 5, 5, 0, 0)
        elif cls.__name__ == "Square":
            dummy = cls(2, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load data from file"""
        filename = cls.__name__ + ".json"
        inst_list = []
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_str = file.read()
                json_list = json.loads(json_str)
                for member in json_list:
                    inst = cls.create(**member)
                    inst_list.append(inst)
        except FileNotFoundError:
            pass
        return inst_list

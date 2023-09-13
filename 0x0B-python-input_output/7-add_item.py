#!/usr/bin/python3
"""
Script contains function that loads, adds and saves to a file
"""
import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


argc = len(argv)
list_items = []
newline = "\n"
try:
    list_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass
finally:
    for idx in range(1, argc):
        list_items.append(argv[idx])

    save_to_json_file(list_items, "add_item.json")

#!/usr/bin/python3
"""
A module
"""

from os import path
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    obj_file = load_from_json_file('add_item.json')
except FileNotFoundError:
    obj_file = []

for arg in argv[1:]:
    obj_file.append(arg)


save_to_json_file(obj_file, 'add_item.json')

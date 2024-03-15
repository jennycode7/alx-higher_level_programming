#!/usr/bin/python3
"""
A module
"""

from os import path
from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if path.exists("add_item.json"):
    obj_file = load_from_json_file("add_item.json")

else:
    obj_file = []
for i in range(1, len(argv)):
    obj_file.append(argv[i])
save_to_json_file(obj_file, "add_item.json")

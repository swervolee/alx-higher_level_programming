#!/usr/bin/python3
"""
A module to read input, put it into a list,
convert the list to JSON, and store it in a file.
"""


from sys import argv
import json
load_from_json = __import__("6-load_from_json_file").load_from_json_file
save_to_json = __import__("5-save_to_json_file").save_to_json_file

new = []

for a in argv[1:]:
    new.append(a)

try:
    old = load_from_json("add_new_item.json")
    save_to_json(new + old, "add_new_item.json")
except FileNotFoundError:
    save_to_json(new, "add_new_item.json")

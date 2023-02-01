#!/usr/bin/python3
"""json file"""
import json


def load_from_json_file(filename):
    """json"""
    with open(filename) as f:
        return json.load(f)

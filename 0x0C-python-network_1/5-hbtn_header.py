#!/usr/bin/python3
"""HBTN Status"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1]).headers.get('X-Request-Id')
    print(req)

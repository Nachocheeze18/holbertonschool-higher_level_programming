#!/usr/bin/python3
"""HBTN Status"""
import requests
import sys


if __name__ == "__main__":
    req = sys.argv[1]
    email = {'email': sys.argv[2]}
    bef = requests.post(req, email)
    print(bef.text)

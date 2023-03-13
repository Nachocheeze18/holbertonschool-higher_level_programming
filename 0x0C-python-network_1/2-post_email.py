#!/usr/bin/python3
"""HBTN Status"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    req = sys.argv[1]
    email = {'email': sys.argv[2]}
    par = parse.urlencode(email).encode('utf-8')
    bef = request.Request(req, par)
    with request.urlopen(bef) as response:
        html = response.read().decode('utf-8')
        print(html)

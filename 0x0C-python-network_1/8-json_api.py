#!/usr/bin/python3
"""HBTN Status"""
import requests
import sys

if __name__ == "__main__":
    req = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    bef = requests.post(req, data={'q': q})
    try:
        moby = bef.json()
        id = moby.get('id')
        name = moby.get('name')
        if len(moby) == 0:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception as err:
        print("Not a valid JSON")

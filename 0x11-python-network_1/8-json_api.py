#!/usr/bin/python3
"""
script posts responses
"""

import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        char = ""
    else:
        char = sys.argv[1]
    
    val = {'q': char}
    r = requests.post(url, data=val)
    try:
        new_json = r.json()
        if new_json:
            print(f"[{new_json.get('id')}] {new_json.get('name')}")
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")

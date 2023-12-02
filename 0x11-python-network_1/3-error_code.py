#!/usr/bin/python3
"""
script sends a request to the URL and displays the body of the response
"""

import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')

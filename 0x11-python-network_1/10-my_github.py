#!/usr/bin/python3
"""
script takes your GitHub credentials and uses the GitHub API to display id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(r.json().get('id'))

#!/bin/bash
# Script displays the size of the body of the response

curl -SI "$1" | grep -i "Content-Length" | awk '{print $2}'
#!/bin/bash
# Use cURL to send an OPTIONS request and display allowed methods

curl -sI "$1" | grep "Allow:" | cut -d ' ' -f 2-
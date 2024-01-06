#!/usr/bin/python3
'prints the x-request-id of a header'
from sys import argv
import urllib.request


url = argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers['X-Request-Id'])

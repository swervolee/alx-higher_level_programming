#!/usr/bin/python3
'prints the x-request-id of a header'
import sys
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))

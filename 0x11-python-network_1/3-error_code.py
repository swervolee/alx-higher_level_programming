#!/usr/bin/python3
'reads a Get and handles errors'
import urllib.request
import sys
from urllib.error import HTTPError


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')

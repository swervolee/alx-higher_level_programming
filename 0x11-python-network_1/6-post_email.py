#!/usr/bin/python3
'Posts an email'
import sys
import requests


if __name__ == '__main__':
    url, email = sys.argv[1:3]
    print(requests.post(url, data={'email': email}).text)

#!/usr/bin/python3
'GITHUB RESTFUL API'
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=basic)
    print(r.json().get('id'))

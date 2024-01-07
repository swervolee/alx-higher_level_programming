#!/usr/bin/python3
'GITHUB RESTFUL API'
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    username, password = sys.argv[1: 3]
    headers = {'Authorization': 'token ' + str(password)}
    url = 'https://api.github.com/user'
    basic = HTTPBasicAuth(username, password)

    r = requests.get(url, auth=basic)

    print(r.json()['id'])

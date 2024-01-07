#!/usr/bin/python3
'GITHUB RESTFUL API'
import sys
import requests


if __name__ == '__main__':
    username, password = sys.argv[1: 3]
    headers = {'Authorization': 'Bearer ' + str(password)}
    print(headers)
    url = 'https://api.github.com/user'

    r = requests.get(url, headers=headers)

    print(r.json()['id'])

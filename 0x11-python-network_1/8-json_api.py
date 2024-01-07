#!/usr/bin/python3
'json read'
import requests
import sys


if __name__ == '__main__':
    try:
        q = sys.argv[1]
    except IndexError as e:
        q = ""

        url = 'http://0.0.0.0:5000/search_user'
        r = requests.post(url, data={'q': q})

        if r.status_code == 204:
            print('No result')
        else:
            try:
                print(r.json())
            except Exception:
                print('Not a valid JSON')

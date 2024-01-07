#!/usr/bin/python3
'GITHUB COMMITS VIA API'
import requests
import sys


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    headers = {'Accept': 'application/vnd.github+json'}
    r = requests.get(url, headers=headers)
    for v, i in enumerate(r.json()):
        print(i.get('commit').get('tree').get('sha') +
              ': ' + i.get('commit').get('author').get('name'))
        if v == 10:
            break

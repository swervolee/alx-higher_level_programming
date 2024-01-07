#!/usr/bin/python3
'GITHUB COMMITS VIA API'
import requests
import sys


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    headers = {'Accept': 'application/vnd.github+json'}
    r = requests.get(url, headers=headers)
    for i in r.json():
        print(i['commit']['tree']['sha'] +
              ': ' + i['commit']['author']['name'])

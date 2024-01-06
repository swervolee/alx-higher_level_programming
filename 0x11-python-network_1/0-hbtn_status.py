#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('http://alx-intranet.hbtn.io/status') as resp:
    body = resp.read()

print(f'Body response:\n\t- type: {type(body)}\n\t- content: {body}')
print(f'\t- utf8 content: {body.decode("utf-8")}')

#!/usr/bin/python3
import urllib.request
req = urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
with req as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))

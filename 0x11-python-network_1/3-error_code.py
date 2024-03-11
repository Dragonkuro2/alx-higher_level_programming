#!/usr/bin/python3
"""
Script that takes in a URL, send a request to URL, and dispaly body
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except urllib.error.HTTPError as er:
        print('Error code: {}'.format(er.code))

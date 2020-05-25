#! /usr/bin/env python3

'''
mapIt.py - Launches a map in the browser using an address
from the command line or clipbaord
'''
import webbrowser, sys, pyperclip

PNAME = sys.argv[0]
GOOGLE_MAPS_URL = 'https://www.google.com/maps/place/'
USAGE_TEXT = f'usage: python3 {PNAME} [address]\n\taddress: use clipboard if omitted'

if len(sys.argv) > 1:
    # Use address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open(GOOGLE_MAPS_URL + address.replace('\n', ' '))

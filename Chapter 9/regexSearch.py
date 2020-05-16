#! /usr/bin/env python3

'''
regexSearch.py

Searches for any line that matches a user-supplied regular expression

Usage: python3 regexSearch.py regex directory
'''

import re, os, sys
from pathlib import Path

USAGE_TEXT = 'usage: python3 regexSearch.py regex directory'

#TODO: Read command line arguments
if len(sys.argv) < 3:
    print(USAGE_TEXT)
    sys.exit(1)

regex = re.compile(sys.argv[1])
directory = sys.argv[2]

#TODO: Validate directory
if directory == '.':
    path = Path.cwd()
else:
    path = Path(directory)
    if not path.is_dir():
        print('%s is not a valid directory.' % (directory))
        sys.exit(1)
    
#TODO: Get all .txt files in a directory
txt_files = list(path.glob('*.txt'))

#TODO: Search for lines that matches user-supplied regex
for txt in txt_files:
    for line in open(txt):
        if regex.findall(line.rstrip()):
            #TODO: Print results to screen
            print(line.rstrip())


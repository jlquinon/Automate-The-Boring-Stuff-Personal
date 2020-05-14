#! /usr/bin/env python3
'''
madlibs.py - Reads text files and lets user add their own text in respective fields

Usage: python3 madlibs.py file1 [file2 ...]

'''

import sys, pyinputplus as pyip

USAGE_TEXT = 'python3 madlibs.py file1 [file2 ...]'
# TODO: Read command line arguments
if len(sys.argv) < 2:
    print(USAGE_TEXT)
    sys.exit(1)
files = sys.argv[1:]

# TODO: Find and open corresponding text files


# TODO: Substitute words from inputs


# TODO: Create result files
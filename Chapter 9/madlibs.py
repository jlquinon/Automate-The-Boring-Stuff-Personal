#! /usr/bin/env python3
'''
madlibs.py - Reads text files and lets user add their own text in respective fields

Usage: python3 madlibs.py file1 [file2 ...]

'''

from pathlib import Path
import sys, pyinputplus as pyip, os, re

USAGE_TEXT = 'usage: python3 madlibs.py file1 [file2 ...]'

# TODO: Read command line arguments
if len(sys.argv) < 2:
    print(USAGE_TEXT)
    sys.exit(1)
files = sys.argv[1:]

# TODO: Find and open corresponding text files
for file in files:
    path = Path(file)
    if not path.is_file():
        print("File %s does not exist!" % (path.name))
    else:
        madlib_file = open(path)
        file_content = madlib_file.read()

        adjective = pyip.inputStr(prompt="Enter an adjective:\n")
        noun1 = pyip.inputStr(prompt="Enter a noun:\n")
        verb = pyip.inputStr(prompt="Enter a verb:\n")
        noun2 = pyip.inputStr(prompt="Enter a noun:\n")

        # TODO: Substitute words from inputs
        adjectiveRegex = re.compile(r'ADJECTIVE')
        nounRegex = re.compile(r'NOUN')
        verbRegex = re.compile(r'VERB')

        sub_content=adjectiveRegex.sub(adjective, file_content)
        sub_content=nounRegex.sub(noun1, sub_content)
        sub_content=verbRegex.sub(verb, sub_content)
        sub_content=nounRegex.sub(noun2, sub_content)

        # TODO: Create result files
        resultFile = open(path.stem +'-result' + path.suffix, 'w')
        resultFile.write(sub_content)

        madlib_file.close()

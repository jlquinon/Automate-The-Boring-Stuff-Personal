#! /usr/bin/env python3

'''
renameDates.py - Renames files with American-style dates to
European-style dates
'''

USAGE_TEXT = 'usage: python3 renameDates.py <directory>'

from pathlib import Path
import re, os, shutil, sys

# TODO: Read command line arguments
if len(sys.argv) < 2:
   print(USAGE_TEXT)
   sys.exit(1)

directory = sys.argv[1]

# TODO: Create a regex that can identify the text pattern of American-style dates.
dateRegex = re.compile(r'''
^(.*?)          # All text before date
((0|1)?\d)-     # One or two digits for the month
((0|1|2|3)?\d)- # One or two digits for the day
((19|20)\d\d)   # Four digits for the yaer
(.*?)$          # All text after the dateRegex
''', re.VERBOSE)

# TODO: Call os.listdir() to find all the files in the working directory.
if not Path(directory).is_dir():
    print('Directory %s does not exist!' % (directory))
    sys.exit(1)

files = os.listdir(directory)

# TODO: Loop over each filename, using the regex to check whether it has a date.
for file_name in files:
    mo = dateRegex.search(file_name)
    if mo:
        before_text = mo.group(1)
        month       = mo.group(2)
        day         = mo.group(4)
        year        = mo.group(6)
        after_text  = mo.group(8)

        eu_date_file = "%s%s-%s-%s%s" % (before_text, day, month, year, after_text)
        # TODO: If it has a date, rename the file with shutil.move()
        americanFileName = Path(directory) / file_name
        euFileName = Path(directory) / eu_date_file

        print(f'Renaming "{americanFileName}" to "{euFileName}"...')
        shutil.move(directory + os.sep + file_name, directory + os.sep + eu_date_file)


#! /usr/bin/env python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard


import pyperclip as pyc
text = pyc.paste()


# TODO: Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]
text = '\m'.join(lines)
pyc.copy(text)
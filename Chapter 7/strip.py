#! /usr/bin/env python3

import re

def regexSub(string, repl='\s'):
    if repl == '\s':
        repl += '*'
        subBeginningRegex = re.compile('^' + repl)
        subEndingRegex = re.compile(repl +'$')

        string = subBeginningRegex.sub('', string)
        string = subEndingRegex.sub('', string)

        return string
    else:
        subRegex = re.compile(repl)
        
        return subRegex.sub('', string)

string1 = '    hello    '
string2 = '  goodbye  '

print(regexSub(string1))
print(regexSub(string2, 'o'))

#! /usr/bin/env python3

spam = ['apples', 'bananas', 'tofu', 'cats']

spam[-1] = 'and ' + spam[-1] 

print(', '.join(spam))
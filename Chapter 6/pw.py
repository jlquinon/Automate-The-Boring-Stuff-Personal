#! /usr/bin/env python3

'''
Python program for a password locker.

Store passwords for different accounts.
'''

import sys, pyperclip as pyc

PASSWORDS = {
    'email' : '24387tTGyugiafqwer',
    'blog'  : 'jHYGW41u7234hgiuqwe',
    'luggage' : '12345'
}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit(1)

account = sys.argv[1]   # First command line arg is the account name

if account in PASSWORDS:
    pyc.copy(PASSWORDS[account])
    print('Password for %s copied to clipboard.' % (account))
else:
    print('There is no account named %s.' % (account))
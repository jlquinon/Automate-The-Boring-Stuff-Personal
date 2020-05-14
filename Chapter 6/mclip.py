#! /usr/bin/env python3

# Multi-Clipboard Automatic Messages

TEXT = {
    'greeting': {
        'reply' : """Hello, %s!\n\nIt is a pleasure to hear from you. I hope all is well on your end.""",
        'initial' : """Hello, $s!\n\nI hope all is well on your end"""
    },
    'closing' : """Thank you in advance for your time. I look forward to hearing back from you at your earliest convenience.""",
    'agree' : """Yes, I agree. That sounds fine to me.""",
    'busy' : """Sorry, can we do this later this week or next week?""",
    'upsell' : """Would you consider making this a monthly donation?"""
}

import sys, pyperclip as pyc

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit(1)

keyphrase = sys.argv[1]     # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyc.copy(TEXT[keyphrase])
    print('Text for %s copied to clipboard.' % (keyphrase))
else:
    print('There is no text for %s' % (keyphrase))
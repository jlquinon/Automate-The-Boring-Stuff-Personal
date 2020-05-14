#! /usr/bin/env python3
#
# mcb.pyw
# Usage: python3 mcb.pyw save <keyword> - Saves clipboard to keyword.
#        python3 mcb.pyw <keyword> - Copies text for keyword to clipboard
#        python3 mcb.pyw list - Copies all keywords to clipboard

import shelve, pyperclip as pyc, sys

USAGE_TEXT = 'usage: python3 mcb.pyw [list] [[save] <keyword>] [delete <keyword>] [clear]'

mclipboard = shelve.open('mclipboard')

# TODO: Read arguments from command line
if len(sys.argv) < 2:
    print(USAGE_TEXT)
    sys.exit(1)

# TODO: Determine action based on arguments provided
command = sys.argv[1]
if command == 'list':
    if len(mclipboard.keys()) == 0:
        print('No contents in clipboard!')
    else:
        pyc.copy(str(list(mclipboard.keys())) + '\n')
        print('Keywords have been copied to clipboard.')
elif command == 'save':
    if len(sys.argv) < 3:
        print(USAGE_TEXT)
        sys.exit(1)
    keyword = sys.argv[2]
    new_text = pyc.paste()
    mclipboard[keyword] = new_text
    print("The text [%s] has been saved under keyword %s." % (new_text.rstrip('\n'), keyword))
elif command == 'delete':
    if len(sys.argv) < 3:
        print(USAGE_TEXT)
        sys.exit(1)
    keyword = sys.argv[2]
    del mclipboard[keyword]
    print("The keyword entry %s has been deleted." % (keyword))
elif command == 'clear':
    mclipboard.clear()
else:
    if command not in mclipboard:
        print('Keyword not found in clipboard')
        sys.exit(1)

    pyc.copy(mclipboard[keyword])

    print('Text for keyword %s has been copied to clipboard.')

mclipboard.close()

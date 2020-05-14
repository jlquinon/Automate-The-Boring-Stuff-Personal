#! /usr/bin/env python3

import time, sys

# How many spaces to indent
indent = 0

# Whether the indentation is increasing or not
indentIncreasing = True


try:
    while True: # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second


        if indentIncreasing:

            # Increase the number of spaces:
            indent += 1

            if indent == 10:
                # Change direction
                indentIncreasing = False


        else:
            # Decrease the number of spaces
            indent -= 1

            if indent == 0:
                # Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

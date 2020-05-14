#! /usr/bin/env python3


import re, pyperclip

# Write regular expression to detect dates in specified format
#
# Format: DD/MM/YYYY
dateRegex = re.compile(r'''
(\d{2})     # DD
/            # / Separator
(\d{2})    # MM
/            # / Separator
(\d{4}) # YYYY
''', re.VERBOSE)


# Store strings into variables
#
# Variables: month, day, year
date = pyperclip.paste()

mo = dateRegex.search(date)

if mo != None:
    day = int(mo.group(1))
    month = int(mo.group(2))
    year = int(mo.group(3))


# TODO: Determine if entered date is valid
#
# Notes:
#   - April, June, September, and November have 30 days
#   - Rest of the months have 31 days
#   - February has 28 days
#   - Feburary has 29 days in an leap year
#       - Leap years are every year divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400
#
    if year < 1000 or year > 2999:
        print("Invalid year range.")
    elif month < 1 or month > 12:
        print("Invalid month range.")
    else:
        # Check proper day ranges
        if day < 1 or day > 31:
            print("Invalid day range.")
        elif day > 30 and (month == 4 or month == 6 or month == 9 or month == 11):
            print("Invalid day for month {}.".format(month))
        elif month == 2:
            if day == 29 and (year % 4 != 0 or year % 400 != 0):
                print("Invalid amount of days for month {}. {} not a leap year.".format(month, year))
            elif day > 28:
                print("Invalid day for month {}.".format(month))

else:
    print("No date found in valid format.")

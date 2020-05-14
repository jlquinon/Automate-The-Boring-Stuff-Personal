#! /usr/bin/env python3


import re, pyperclip


# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
(\d{3}|(\(\d{3}\)))?       # area code (optional)
(\s|-|\.)?                         # first separator
(\d{3})                         # first 3 digits
(\s|-|\.)                              # separator
(\d{4})                       # last 4 digits
(\s*((ext(\.)?)\s*|x)              # extension word-part (optional)
 (\d{2,5}))?                   # extension number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+ # name part
@               # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
\.[a-zA-Z]{2,4} # dot-something
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = list()

for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = 'Phone Numbers\n' + '\n'.join(allPhoneNumbers) + '\nEmails\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

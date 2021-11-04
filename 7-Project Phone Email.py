# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:32:05 2019

@author: MooreN
"""

# modules that we love
import pyperclip
import re

# regex for phone numbers
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# regex for email addresses
email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+             # username
        @                             # @ symbol
        [a-zA-Z0-9.-]+                # domain name
        (\.[a-zA-Z]{2,4})             # dot-something
        (\.[a-zA-Z]{2})?              # maybe a top level domain        
        )''', re.VERBOSE)

# get the text off the clipboard
text = str(pyperclip.paste())

matches = []

# find all phone numbers and email addresses in the text
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text): 
    matches.append(groups[0])

# format the strings back into a nice form 
# put them onto the clipboard   
# display a message if no matches were found    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No matches found for phone number or email address')
    



# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:14:36 2019

@author: MooreN
"""

# add bullet points to a copied list from the clipboard 
# and put it back on the clipboard

import pyperclip

myList = pyperclip.paste()

print(myList)

splitList = myList.split('\r\n')

print('')
print(splitList)

for i in range(len(splitList)):
    splitList[i] = '* ' + splitList[i]
    
print('')
print(splitList)

copier = '\n'.join(splitList)

pyperclip.copy(copier)
print('')
print(copier)
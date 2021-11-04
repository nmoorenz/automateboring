# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:21:34 2019

@author: MooreN

  # mcb.pyw - Saves and loads pieces of text to the clipboard.
  # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
  #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
  #        py.exe mcb.pyw list - Loads all keywords to clipboard.
  
mcb.bat
@pyw.exe C:\Python34\mcb.pyw %*

https://stackoverflow.com/questions/47425520/activate-virtualenv-and-run-py-script-from-bat

"""

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')


if len(sys.argv) == 3: 
    if sys.argv[1].lower() == 'save':
        # save clipboard content
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        # delete saved arguments
        if sys.argv[2] in mcb_shelf:
            mcb_shelf.pop[sys.argv[2]]
elif len(sys.argv) == 2: 
    if sys.argv[1].lower() == 'list': 
        # list keywords
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf: 
        # load the item to the clipboard
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        for mcb_keys in mcb_shelf:
            mcb_shelf.pop(mcb_keys)
        

mcb_shelf.close()


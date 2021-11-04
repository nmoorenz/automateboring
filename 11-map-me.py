# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:09:07 2019

@author: MooreN
"""

#! python3
# 11-map-me.py - Launches a map in the browser with inputs
# command line or clipboard inputs

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
else:  
    # get address from clipboard
    address = pyperclip.paste()
    
    
webbrowser.open('https://www.google.com/maps/place/' + address)


    
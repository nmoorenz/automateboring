# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:31:55 2020

@author: MooreN
"""

# break and continue

while True: 
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue                                # jump back to the beginning
    print('Hello Joe. What is the fishy password?')
    password = input()
    if password.lower() == 'swordfish':
        break                                   # jump out of the loop
print('Access Granted')
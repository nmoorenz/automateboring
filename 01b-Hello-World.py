# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:56:43 2020

@author: MooreN
"""

#####
# Your first program
#####

# this program asks for the user's name

print('Hello You!')

print('What is your name?')
myName = input()
print('It is good to meet you ' + myName)
print('Your name has ' + str(len(myName)) + ' letters')

print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')
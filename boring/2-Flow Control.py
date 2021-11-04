# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:07:07 2019

@author: MooreN
"""

# flow control

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
    
    
name = ''
while name != 'your name':
     print('Please type your name.')
     name = input()
print('Thank you!')


print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
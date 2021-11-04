# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:07:07 2019

@author: MooreN
"""

# flow control

# Boolean
True
False

# relational operators
42 == 42
42 != 42
42 >= 42
42 < 42

'spam' == 'eggs'
'spam' > 'eggs'
'camelot' != 'Arthur'

# Boolean operators
True and True
True and False
False or True
False or False

False or not False
True and not True

(42 == 42) and (6 < 9) 

# conditions and blocks
name = 'spam'
if name == 'spam':
    print('yeah, you got it')

# if statements
# see 02b-vampire.py

# while loops
bacon = 0
while bacon < 5:
    bacon += 1
    print(bacon)

# the most annoying loop
name = ''
while name != 'your name':
     print('Please type your name')
     name = input()
print('Thank you!')

# break
bacon = 0
while True:
    bacon += 1
    print(bacon)
    if bacon > 5: 
        break

# for loops
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
    
total = 0
for x in range(101):
    total += x
print(total)    
    
total = 0
x = 0
while x < 101:
    total += x
    x += 1
print(total)    
    
# start, stop, increment    
for i in range(99, 42, -5):
    print(i)    
    
import random, sys, os, math

for i in range(10):
    print(random.randint(0,i))
    
# exit call
while 1==1:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('you typed ' + response)
    
    
    
    
    
    
    
    
    
    
    
    
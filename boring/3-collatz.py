# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:45:31 2019

@author: MooreN
"""

def collatz(number):
    # if this is an infinite loop then we can win a Nobel prize
    num_orig = number
    i = 0
    while number != 1:
        if number % 2 == 0: # even
            print(number // 2)
            number = number // 2
            i += 1
        else: 
            print(3 * number + 1)
            number = 3 * number + 1
            i += 1
    print('The total stopping time of ' + str(num_orig) + ' is ' + str(i) + ' steps')
        
    
print('Let\'s try the Collatz sequence! Enter a number: ')
try: 
    myNum = int(input())
except ValueError: 
    print('Please enter a number')

collatz(myNum)
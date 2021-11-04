# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:27:31 2019

@author: MooreN
"""
##### raise an exception
raise Exception("The text said to put this in the immediate window")

# make sure of functions arguments and deal with problems nicely
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
    
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))
        

##### functions call other functions
        
def spam():
    bacon()
    
def bacon():
    raise Exception('This is the error message')
    
spam()
        
##### traceback

import traceback

try:
    raise Exception('this is the error message.')
except:
    error_file = open('error_info.txt', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('the traceback info was written to error_info.txt.')
    
##### assert statement for programmer errors

pod_bay_door_status = 'open'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open"'
pod_bay_door_status = "I'msorry, Dave. I'm afraid I can't do that."
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open"'

# really important to have at least one red light at an intersection

#### logging module

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug('start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(6))

logging.debug('End of program')

# remove logging messages with 
logging.disable(logging.CRITICAL)

# levels of logging
logging.debug('Some debugging details')
logging.info('The logging module is working as intended')
logging.warning('An error message is about to be displayed')
logging.error('An error has occurred')
logging.critical('The program i unable to recover!')

# logging to a file
logging.basicConfig(filename='my_program_log.txt', lovel=logging.DEBUG, format='%(asctime)s - %levelname)s - %(message)s')

# 10-buggy-adding-program.py created in IDLE
    
# coin flip
import random

heads = 0

for i in range(1,1001):
    if random.randint(0,1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')
    
print('Heads came up ' + str(heads) + ' times.')






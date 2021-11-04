# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:36:46 2019

@author: MooreN
"""

import os

os.path.join('users', 'mooren', 'r-work')

my_files = ['numbers.txt', 'alpha.csv', 'nonsense.zip']

for filename in my_files:
    print(os.path.join('c:\\users\\mooren', filename))
    
# current working directory
    
os.getcwd()

os.chdir('C:\\Windows\\temp')

os.getcwd()

# use . to refer to the current working directory, 
# use .. to refer to the parent directory

os.chdir('C:\\Users\\mooren\\r-work\\automateboring')

os.chdir('..\\..\\')

os.getcwd()

# os.makedirs() to make a directory

os.chdir('r-work')
os.chdir('automateboring')

cwd = os.getcwd()

os.makedirs('fake\\experiment\\unnecessary')

# absolute and relative

os.path.abspath('fake')

os.path.isabs('fake')

os.path.isabs(os.getcwd())

os.path.relpath('r-work', 'C:\\Users')

os.path.abspath('.')

os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')

this_file = 'C:\\Users\\mooren\\r-work\\automateboring\\8-read write files.py'

os.path.basename(this_file)

os.path.dirname(this_file)

os.path.split(this_file)

## file sizes and folder contents

os.path.getsize(cwd + '\\8-read write files.py')

os.listdir(cwd)

# join these together for total file size

total_size = 0

for filename in os.listdir(cwd):
    total_size = total_size + os.path.getsize(os.path.join(cwd, filename))

# checking validity
    
os.path.exists('Z:\\Desktop')

os.path.exists('C:\\nonsense')

os.path.isdir(cwd)

os.path.isfile(cwd)

os.path.isdir('C:\\Windows\\System32\\calc.exe')

os.path.isfile('C:\\Windows\\System32\\calc.exe')

### file read and write process

hello_file = open('8-tester.txt')

hello_content = hello_file.read()

hello_content

hello_file.close()

sonnet_18 = open('8-sonnet18.txt')

sonnet_lines = sonnet_18.readlines()

sonnet_18.close()

## writing to files

bacon_file = open('8-bacon.txt', 'w')
bacon_file.write('Hello Bacon!\n')
bacon_file.close()

bacon_file = open('8-bacon.txt', 'a')
bacon_file.write('I love bacon')
bacon_file.close()

bacon_file = open('8-bacon.txt')
bacon_text = bacon_file.read()
bacon_file.close()
print(bacon_text)

## save variables with SHELVE module

import shelve

shelf_file = shelve.open('mydata')
cats = ['Sophie', 'Tilly', 'Panda']
shelf_file['cats'] = cats
shelf_file.close()

shelf_info = shelve.open('mydata')
type(shelf_info)
shelf_info['cats']

list(shelf_info.keys())
list(shelf_info.values())

shelf_info.close()

## save variables PPRINT.PFORMAT

import pprint

cats = [{'name' : 'Sophie', 'desc' : 'chubby'}, {'name' : 'Panda', 'desc' : 'cute'}]
pprint.pformat(cats)

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

import myCats

myCats.cats
myCats.cats[0]






















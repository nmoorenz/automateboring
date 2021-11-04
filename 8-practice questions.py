# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:59:25 2019

@author: MooreN
"""

'''
Q:1. What is a relative path relative to?

The current working directory
'''
'''
Q:2. What does an absolute path start with?

a drive letter 
'''
'''
Q:3. What do the os.getcwd() and os.chdir() functions do?

get current working directory, change current directory
'''
'''
Q:4. What are the . and .. folders?

current working directory, parent directory
'''
'''
Q:5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

dir name: C:\bacon\eggs
base name: spam.txt
'''
'''
Q:6. What are the three “mode” arguments that can be passed to the open() function?

read, write, append (r, w, a)
'''
'''
Q:7. What happens if an existing file is opened in write mode?

let's see! 
indeed, makes it blank
'''
myfile = open('8-sonnet18 - Copy.txt', 'w')
myfile.close()

'''
Q:8. What is the difference between the read() and readlines() methods?

read gets one string, readlines returns a list, one element for each line
'''
'''
Q:9. What data structure does a shelf value resemble?

resembles a dictionary with keys and values (but not real lists for the keys)
'''
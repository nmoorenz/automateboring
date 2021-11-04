# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:46:53 2019

@author: MooreN
"""

'''
Q:1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

'''
spam = 50
assert spam>=10, 'spam should be 10 or more'

'''
Q:2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
'''
eggs = 'spam'
bacon = 'SPam'
assert eggs.lower() != bacon.lower(), 'eggs and bacon should be different'

'''
Q:3. Write an assert statement that always triggers an AssertionError.
'''
assert 1 == 0, 'obvious error'
'''
Q:4. What are the two lines that your program must have in order to be able to call logging.debug()?
'''
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %levelname)s - %(message)s')
'''
Q:5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
'''
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(asctime)s - %levelname)s - %(message)s')

'''
Q:6. What are the five logging levels?
'''
levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

'''
Q:7. What line of code can you add to disable all logging messages in your program?
'''
logging.disable(logging.CRITICAL)

'''
Q:8. Why is using logging messages better than using print() to display the same message?
'''
answer = 'You can turn off logging with one line, rather than commenting print statements'

'''
Q:9. What are the differences between the Step, Over, and Out buttons in the Debug Control window?

Step into functions, step over functions, run until function finished
'''

'''
Q:10. After you click Go in the Debug Control window, when will the debugger stop?

Whenever it wants to, i.e. exception or error or breakpoint
'''

'''
Q:11. What is a breakpoint?

A place to pause and take a breath
'''

'''
Q:12. How do you set a breakpoint on a line of code in IDLE?
Right click > Set Breakpoint
'''
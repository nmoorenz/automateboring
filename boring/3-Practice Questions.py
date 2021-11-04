# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:22:19 2019

@author: MooreN
"""

"""
1.
Why are functions advantageous? 

Reusable code! 
"""
"""
2. 
when does the code in a function execute? 
When it is defined or when it is called? 

Called
"""
"""
3. 
what statement creates a function? 

def
"""
"""
4.
difference between a function and a function call

function is the section of code, function call is done to use that code
"""
"""
5.
How many global scopes are there in a Python program? How many local scopes?

one global scope, as many local scopes as there are functions
"""
"""
6.
What happens to variables in a local scope when the function call returns?

Washed away, no longer exists
"""
"""
7.
What is a return value? Can a return value be part of an expression? 

the value returned from a function, can be an expression
"""
"""
8.
If a function does not have a return statement, what is the return value of a call to that function?

returns None
"""
def no_return(x,y):
    c = x + y

res = no_return(4,5)
print(res)

"""
9.
How can you force a variable in a function to refer to the global variable?

use something like: 
    global spam
"""
"""
10.
What is the data type of None?

NoneType
"""
"""
11.
What does the import areallyourpetsnamederic statement do?

import the python module areallyourpetsnamederic and all its functions
"""
"""
12.
If you had a function named bacon() in a module named spam, 
how would you call it after importing spam?

spam.bacon()
"""
"""
13.
How can you prevent a program from crashing when it gets an error?

do some data validation to find common problems, then use try except
"""
"""
14.
What goes in the try clause? What goes in the except clause?

try: 
    the thing that might cause an error
except:
    the other possibility or an error message
"""










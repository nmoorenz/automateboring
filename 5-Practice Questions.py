# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:09:45 2019

@author: MooreN
"""

"""
Q:1. What does the code for an empty dictionary look like?

my_dict = {}

Q:2. What does a dictionary value with a key 'foo' and a value 42 look like?

bar = {'foo': 42}

Q:3. What is the main difference between a dictionary and a list?

dictionary: no order, key-value pair; list: ordered, sliced

Q:4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

key error

Q:5. If a dictionary is stored in spam, what is the difference 
between the expressions 'cat' in spam and 'cat' in spam.keys()?

no difference

Q:6. If a dictionary is stored in spam, what is the difference 
between the expressions 'cat' in spam and 'cat' in spam.values()?

gotta look at the values specifically if we want to look at values, 
otherwise looking in keys

Q:7. What is a shortcut for the following code?

if 'color' not in spam:
    spam['color'] = 'black'
    
spam.get('color', 'black') 
    
Q:8. What module and function can be used to “pretty print” dictionary values?

pprint.pprint()
"""

spam = {'bar': 100}
spam['foo']

spam['cat'] = 99

'cat' in spam

spam['dict'] = 'cat'

'cat' in spam.values()

if 'color' not in spam:
    spam['color'] = 'black'
    
spam.get('color', 'white') 

pprint.pprint(spam)

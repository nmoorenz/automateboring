# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:59:26 2019

@author: MooreN
"""

"""
1.
Two types of boolean values

True False
"""
"""
2. 
what are the three boolean operators? 

and, or, not
"""
""" 
3.
Write out truth tables for each operator and their evaluation

True and True = True
True and False = False
False and False = False

True or True = True
True or False = True
False or False = False

not True = false
not False = True
"""
"""
4.
(5 > 4) and (3 == 5)
False

not (5 > 4)
False

(5 > 4) or (3 == 5)
True

not ((5 > 4) or (3 == 5))
False

(True and True) and (True == False)
False

(not False) or (not True)
True
"""
"""
5
what are the six comparison operators? 

=
!=
<
<=
>
>=
"""
"""
7.
Explain what a condition is and where you would use one

Flow Control! if statement to make the code inside run, perhaps with multiple
conditions with elif and finally else

Where statement, waiting for a condition to become true

"""
"""
8.
spam = 0                  block 1  
if spam == 10:                   
    print('eggs')         }        
    if spam > 5:          }
        print('bacon')    }          } block 2
    else:                 }
        print('ham')      }          } block 3 
    print('spam')         }
print('spam')            
"""
"""
9.
Write code that prints Hello if 1 is stored in spam, 
prints Howdy if 2 is stored in spam, 
and prints Greetings! if anything else is stored in spam.

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else: 
    print('Greetings!')
    
"""
"""
10. 
Exit an infinite loop with ctrl+c
"""
"""
11.
difference between break and continue

break gets out of a loop or conditional completely, 
continue jumps back to the start of the loop
"""
"""
12.
What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

no difference!
"""
"""
13.
Write a short program that prints the numbers 1 to 10 using a for loop. 
Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

for x in range(1, 11): 
    print(x)
    
i = 1
while i <= 10:
    print(i)
    i += 1
    
"""

for x in range(1, 11): 
    print(x)

i = 1
while i <= 10:
    print(i)
    i += 1

"""
14.
If you had a function named bacon() inside a module named spam, 
how would you call it after importing spam?

from module import bacon
"""





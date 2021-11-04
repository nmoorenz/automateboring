# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:44:31 2019

@author: MooreN
"""

"""
1.
what is []?

an empty list
"""
"""
2. 
How would you assign the value 'hello' as the third value in a list stored 
in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
"""
spam = [2, 4, 6, 8, 10]

spam[2] = 'hello'

print(spam)

"""
For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
"""
spam = ['a', 'b', 'c', 'd']

"""
3. 
What does spam[int(int('3' * 2) // 11)] evaluate to?

spam[int(int('33')) // 11)]
spam[int(33) // 11)]
spam[3]
'd'
"""
spam[int(int('3' * 2) // 11)]

"""
4.
What does spam[-1] evaluate to?

'd'
"""
spam[-1]

"""
5.
What does spam[:2] evaluate to?

['a', 'b']
"""
spam[:2]

"""
For the following three questions, let’s say bacon contains 
the list [3.14, 'cat', 11, 'cat', True].
"""
bacon = [3.14, 'cat', 11, 'cat', True]

"""
6.
What does bacon.index('cat') evaluate to?

1
"""
bacon.index('cat')

"""
7.
What does bacon.append(99) make the list value in bacon look like?

[3.14, 'cat', 11, 'cat', True, 99]
"""
bacon.append(99)
print(bacon)

"""
8.
What does bacon.remove('cat') make the list value in bacon look like?

first entry only
[3.14, 11, 'cat', True, 99]
"""
bacon.remove('cat')
print(bacon)

"""
9.
What are the operators for list concatenation and list replication?

+ joins, * multplies
"""
"""
10.
What is the difference between the append() and insert() list methods?

append at the end, insert at a position
"""
"""
11.
What are two ways to remove values from a list?

spam.remove() and del spam[2]
"""
"""
12.
Name a few ways that list values are similar to string values.

concatenation, replication, indexing, many methods
"""
"""
13. 
What is the difference between lists and tuples?

lists [] mutable; tuples () immutable
"""
"""
14.
How do you type the tuple value that has just the integer value 42 in it?

answer = (42,)
"""
answer = (42,)

"""
15.
How can you get the tuple form of a list value? 
How can you get the list form of a tuple value?

tuple() and list() functions
"""
tuple(bacon)
list(answer)

"""
16.
Variables that “contain” list values don’t actually contain lists directly. 
What do they contain instead?

a reference to that list in memory
"""
"""
17.
What is the difference between copy.copy() and copy.deepcopy()?

deepcopy() copies the lists that are within the list
"""











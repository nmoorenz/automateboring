# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:13:59 2019

@author: MooreN

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string 
with all the items separated by a comma and a space, with and inserted before 
the last item. For example, passing the previous spam list to the function 
would return 'apples, bananas, tofu, and cats'. But your function should be 
able to work with any list value passed to it.
"""

spam = ['apples', 'bananas', 'tofu', 'cats']
eggs = ['apples']
bacon = ['apples', 'bananas']
cheese = ['apples', 'bananas', 'tofu', 'cats', 'rat', 'bat', 'mat']
zero = []
digit = 5

def oxfordComma(myList): 
    if type(myList) != list:
        return 'Error: argument is not a list'
    else:
        lenList = len(myList)
        if lenList == 0:
            return 'Error: list has no elements' 
        elif lenList == 1: 
            return myList[0]
        elif lenList == 2:  
            return myList[0] + ' and ' + myList[1]
        else: # three or more
            oxList = ''
            for i in range(lenList - 1):
                oxList += myList[i] + ', '
            oxList += 'and ' + myList[lenList - 1]
            return oxList
        
print(oxfordComma(cheese))


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

"""
Copy the previous grid value, and write code that uses it to print the image.


..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

"""

for i in range(len(grid[0])): 
    for j in range(len(grid)): 
        print(grid[j][i], end = ' ')
    print('\n')








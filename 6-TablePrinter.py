# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:08:17 2019

@author: MooreN
"""

# input data
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# function
def printTable(tableList):
    colWidths = [0] * len(tableList)
    # get the longest string for each column
    for i in range(len(tableList)):
        for j in tableList[i]:
            if len(j) > colWidths[i]:
                colWidths[i] = len(j)
    print(colWidths)       
    # print the table
    for i in range(len(tableList[0])):
        for j in range(len(tableList)):
            print(tableList[j][i].rjust(colWidths[j]), end = ' ')
        print('')
        
        
       
printTable(tableData)
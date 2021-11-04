# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:16:17 2020

@author: MooreN
"""

# imports
import random
import sys

# possibilities
moves = {'r' : 'ROCK', 'p' : 'PAPER', 's' : 'SCISSORS'}
# game introduction
print(', '.join(list(moves.values())))

# dictionary for a too complicated way of recording results
results = {'Wins' : 0, 'Losses' : 0, 'Ties' : 0}

# loop for as long as necessary
while True:
    while True:
        # ask for a response
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        # get the input
        move = input()
        if move in moves.keys():
            print(moves[move] + ' versus...')
            break
        elif move == 'q':
            sys.exit()
        else: 
            print('Not a valid move, please type one of p, r, s, or q')
        
    # computer move
    comp = random.choice(list(moves.keys()))
    # print computer move
    print(moves[comp])
        
    # conditional result
    if move == comp:
        print('It is a tie!')
        results['Ties'] += 1
    elif (move == 'r' and comp == 's') or (move == 'p' and comp == 'r') or (move == 's' and comp == 'p'):
        print('You win!')
        results['Wins'] += 1
    elif (move == 'r' and comp == 'p') or (move == 'p' and comp == 's') or (move == 's' and comp == 'r'):
        print('You lose!')
        results['Losses'] += 1    
        
    print(str(results['Wins']) + ' Wins, ' + str(results['Losses']) + ' Losses, ' + str(results['Ties']) + ' Ties')
    print()
    
    
    
    
    
    
    
    
    
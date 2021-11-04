# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:33:07 2019

@author: MooreN
"""

# random number guesser

import random

# 1 is always the lowest number
highest = 20

print('I am thinking of a number between 1 and ' + str(highest))

answer = random.randint(1, highest)
guess = 0
numGuess = 0

while numGuess < 8:
    print('Take a guess.')
    guess = int(input())
    numGuess += 1
    if guess < answer: 
        print('Your guess is too low')
    elif guess > answer: 
        print('Your guess is too high')
    else: # correct
        break
if guess == answer:
    print('Good job! You guessed my number in ' + str(numGuess) + ' guesses!')
else: 
    print('You took too many guesses! The number I was thinking of was ' + str(answer))
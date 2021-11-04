# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:59:46 2020

@author: MooreN
"""

import random

low = 1
high = 20

num = random.randint(low,high)

print("I am thinking of a number between " + str(low) + " and " + str(high) + ".")


for guess_num in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < low or guess > high:
        print('Your guess is not even in the right range!')
    elif guess < num:
        print('Your guess is too low')
    elif guess > num:
        print('Your guess is too high')
    else: 
        break
        
if guess == num:
    print('Great effort! You took ' + str(guess_num) + ' guesses.')   
else:
    print('Nope, you took too many guess. I was thinking of ' + str(num))


# guess_num = 0
# while True:
#     print('Take a guess')
#     guess = input()
#     try:
#         guess = float(guess)
#     except:
#         print('enter a number please')
#     guess_num += 1
#     if guess == num:
#         print('Great effort! You took ' + str(guess_num) + ' guesses.')
#         break
#     elif guess < low or guess > high:
#         print('Your guess is not even in the right range!')
#     elif guess < num:
#         print('Your guess is too low')
#     elif guess > num:
#         print('Your guess is too high')
#     elif type(guess) != 'int':
#         print('You are going to have to enter an integer to be successful')
#     else: 
#         print('I do not know how we got here')
        
    

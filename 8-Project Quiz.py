# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:23:40 2019

@author: MooreN

randomQuizGenerator.py - Creates quizzes with questions and answers in
random order, along with the answer key.

"""

import random
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    
#os.makedirs(os.getcwd() + '\\quiz')
os.chdir(os.getcwd() + '\\quiz')
   
for quiznum in range(35):

    # create file pointers for questions and answers
    quizfile = open('capitalsquiz%s.txt' % (quiznum + 1), 'w')
    answerkeyfile = open('capitalsquiz_answer%s.txt' % (quiznum + 1), 'w')
    
    # write out the header for the quiz
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiznum + 1))
    quizfile.write('\n\n')
    
    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    
    # loop through all 50 states, making a question for each
    for question_num in range(50): 
        # get right and wrong answers
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)
        
        # write the questions and answers to the quiz file
        quizfile.write('%s. What is the capital of %s?\n' % (question_num + 1, states[question_num]))
        for i in range(4): 
            quizfile.write(' %s. %s \n' %('ABCD'[i], answer_options[i]))
        
        quizfile.write('\n')
        
        # write the answers in the answerkeyfile
        answerkeyfile.write('%s. %s\n' % (question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))
    
    quizfile.close()
    answerkeyfile.close()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
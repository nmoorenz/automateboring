# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:10:01 2019

@author: MooreN
"""

# define our types
word_types = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

# open file, read sentence, close file
mad = open('mad_libs.txt')
sentence = mad.readlines()
mad.close()

# split into words
words = str(sentence).split()

# replacement string
replacement = ''

# search for word types within sentence
for i in range(len(words)):
    #print(word)
    if words[i] in word_types: 
        while replacement == '':  
            # ask user for those words
            replacement = input('Please give me a %s: \n' % words[i])
        # use the replacement to replace 
        words[i] = replacement
        replacement = ''

# print to screen and save new file    
new_sentence = ' '.join(words)
        
print(new_sentence)




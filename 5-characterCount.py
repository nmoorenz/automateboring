# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:06:56 2019

@author: MooreN
"""
import pprint

message = 'The quick brown fox jumps over the lazy dog.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)


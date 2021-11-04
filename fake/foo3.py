# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:35:59 2019

@author: MooreN
"""

# Suppose this is foo3.py.

def functionA():
    print("a1")
    from foo3 import functionB
    print("a2")
    functionB()
    print("a3")

def functionB():
    print("b")

print("t1")
print("m1")
functionA()
print("m2")
print("t2")
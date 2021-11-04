# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:36:30 2019

@author: MooreN
"""

# Suppose this is in foo4.py
__name__ = "__main__"

def bar():
    print("bar")

print("before __name__ guard")
if __name__ == "__main__":
    bar()
print("after __name__ guard")
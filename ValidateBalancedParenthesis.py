# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 21:50:19 2019

@author: Anuj
"""

s = "(()[])]"
bracket_map = {'(':')',
               '{':'}',
               '[':']',
               '"':'"'
               }
open_par = set(["(","[","{",'"'])
stack = []
for i in s:
    if i in open_par:
        stack.append(i)
    elif stack and i == bracket_map[stack[-1]]:
        stack.pop()
    else:
        print(False)
   
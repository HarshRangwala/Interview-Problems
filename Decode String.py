# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:30:29 2019

@author: Anuj
"""

def decodeString(s):
  # Fill this in.
  stack = []
  for char in s:
      if char != ']':
          stack.append(char)
          print("1Stack   :",stack)
      else:
          temp = ''
          while stack:
              x = stack.pop()
              if x == '[':
                  n = ''
                  while stack and stack[-1].isdigit():
                      n = stack.pop() + n
                      print("n     :",n)
                  stack.append(temp * int(n))
                  break
              else:
                  temp = x+temp
  return ''.join(stack) 

print(decodeString('23[a2[b]c]'))
# abbcabbc
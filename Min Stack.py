# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:47:38 2019

@author: Anuj
"""

class minStack(object):
  def __init__(self):
    # Fill this in.
    self.stack = []

  def push(self, x):
    # Fill this in.
    self.stack.append(x)


  def pop(self):
    # Fill this in.
    if self.stack:
        self.stack.pop()    

  def top(self):
    # Fill this in.
    if self.stack:
        top = self.stack.pop()
        self.stack.append(top)
        return top

  def getMin(self):
    # Fill this in.
    
    return min(self.stack)

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
#print("STACK    ",x.stack)
print(x.getMin())
# -3
x.pop()
#print("STACK    ",x.stack)
#print(x.stack[x.top])
print(x.top())
# 0
print(x.getMin())
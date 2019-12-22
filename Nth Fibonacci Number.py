# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:38:59 2019

@author: Anuj
"""

class Solution():
  def fibonacci(self, n):
    # fill this in.
    if n==0:
        return n
    elif n==1 or n == 2:
        return 1
    elif n>2:
        a,b = 1,1
        for i in range(3, n+1):
            c = a+b
            #print(c)
            a = b
            #print(a)
            b = c
            #print(c)
        return c

n = 7
print(Solution().fibonacci(n))
# 34
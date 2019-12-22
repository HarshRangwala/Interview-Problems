# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:29:12 2019

@author: Anuj
"""
class Solution():
  def plusOne(self, digits):
    # Fill this in.
    v = []
    x = int("".join(map(str, digits)))+1
    for x in str(x):
        v.append(int(x))
    return v
    
num = [9,9,9]
print(Solution().plusOne(num))
# [3, 0, 0]


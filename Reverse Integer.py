# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:51:56 2019

@author: Anuj
"""

class Solution:
  def reverse(self, x):
    # Fill this in.
    if x > 0:
        a = int(str(x)[::-1])
    if x < 0:
        a = -int(str(x*-1)[::-1])
    minimum = -2**31
    maximum = 2**31-1
    if a not in range(minimum, maximum):
        return 0
    else:
        return a
    

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0

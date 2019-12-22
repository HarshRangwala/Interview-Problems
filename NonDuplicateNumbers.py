# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:20:32 2019

@author: Anuj
"""

def singleNumber(nums):
  # Fill this in.
  count = 0
  #sort
  v = sorted(nums)
  for i in range(1, len(v)):
      if v[i-1] == v[i]:
          count +=1
      else:
          count -=1
      if count == -1:
          return v[i-1]
      return v[-1]
print( singleNumber([9,2,3,5,9,5,12,3, 2, 4,4,9, 3, 2, 1,1]))
# 1
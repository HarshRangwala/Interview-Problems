# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:36:41 2019

@author: Anuj
"""
def findKthLargest(nums, k):
  # Fill this in.
  v = []
  for i in range(k):
      v.append(nums[i])
  return max(v)

print(findKthLargest([3,2,1,5,6,4],2))
# 5

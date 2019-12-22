# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 02:03:24 2019

@author: Anuj
"""
'''
Data Structure: set
Step1 : I am going to check if the elements on the list is visited or not. 
      If the element is visited I would then add'em to the list. 
      var - visited
      type - list

'''
def longest_consecutive(nums):
  # Fill this in.
  if not nums:
      return 0
  visited = set()
  nums = set(nums)
  count = 0
  for index in range(len(nums)):
      

          
print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4
# 4
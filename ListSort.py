# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:28:03 2019

@author: Anuj

"""
'''
a = [1,2,3,3,1,2,3]
v = sorted(a)
print(v)
u = len(set(a))
print(u)'''

def sortNums(nums):
    if len(set(nums))> 3:
        return "Try Again"
    else:
        #Sorting
        v = sorted(nums)
        return v
print(sortNums([3, 3, 2, 1, 3, 2, 1,2]))

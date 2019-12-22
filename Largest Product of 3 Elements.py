# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:05:57 2019

@author: Anuj
"""
'''
l = [-4, -4, 2, 8]
for i in range(len(l)):
    for j in range(i+1):
        print(l[i]*l[j])
    '''
class Solution:
    def maximumProduct(self, nums) :
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])
print(Solution.maximumProduct("",[4,1,2,3]))
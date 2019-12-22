# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:18:26 2019

@author: Anuj
"""
nums = [0,1,0,3,12]
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] , nums[i]=nums[i] , nums[pos]
                pos += 1
                
        return nums
print(Solution.moveZeroes("",nums))
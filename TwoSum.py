# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:05:07 2019

@author: Anuj
"""

#You are given a list of numbers, and a target number k.
#Return whether or not there are two numbers in the list that add up to k.
class Solution:
    def twoSum(self, nums, target):
        '''
        dictionary = {}

        for index, num in enumerate(nums):
            other = target - num
            print(other)
            print(dictionary)

            print(index)
            if other in dictionary:
                return True #[dictionary[other], index]
            else:
                dictionary[num] = index
                print("---",dictionary[num])
                print("-------",index)
        return []
        '''
        '''
        if len(nums)<2:
            pass
        r = list()
        for i in range(len(nums)):
            comp = target - nums[i]
            print(comp,"=comp",target,"-",nums[i])
            print("Value of",r)
            if comp in r:
                return [i, nums.index(comp)]
            r.append(nums[i])

'''















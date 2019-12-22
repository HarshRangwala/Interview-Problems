# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:29:49 2019

@author: Anuj
"""

import matplotlib.pyplot as plt


def sortNums(nums):
    if len(set(nums))> 3:
        return "Try Again"
    else:
        #Sorting
        v = sorted(nums)
        plt.plot(v)
        return v

print(sortNums([3, 2,1]))
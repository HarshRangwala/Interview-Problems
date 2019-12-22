# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 02:32:34 2019

@author: Anuj
"""


class Solution(object):
  def findSingle(self, mylist):
    # Fill this in.
    '''
    m = sorted(set([i for i in mylist if mylist.count(i)<2]))
    return m
    '''
    count = 0
    for i in mylist:
        count ^= i
    return count

        
            

mylist=[7, 3, 5, 5, 4, 3, 4, 8, 8]
print(Solution().findSingle(mylist))
# 3
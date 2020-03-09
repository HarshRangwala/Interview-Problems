# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 11:48:05 2020

@author: Anuj
"""

num= [-1,0,3,5,9,12]
#num = sorted(num)
target = 90
'''
low = 0
high = len(num) - 1
#mid = (low+high)//2
print(low)
print(high)

while low<=high:
    mid = (low+high)//2
    if num[mid]<target:
        low = mid + 1
    elif num[mid]>target:
        high = mid - 1
    else:
        print(mid)
        break
    print(-1)
'''
class Solution(object):
    def search(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(num) - 1
        
        while low<=high:
            mid = (low+high)//2
            if num[mid]<target:
                low = mid + 1
            elif num[mid]>target:
                high = mid -1
            else:
                return mid
        return -1

print(Solution.search(0, num, target))


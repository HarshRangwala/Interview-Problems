# -*- coding: utf-8 -*-
"""
Created on Sat May  2 14:14:03 2020

@author: Anuj
"""


mat = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30],
]
class Solution:
    def searchMatrix(self, mat, target):
        if not len(mat) or not len(mat[0]):
            return False
        height = len(mat)       #h
        width = len(mat[0])     #w
        for row in range(len(mat)):
            if mat[row][0]<= target<=mat[row][-1]:
                low = 0
                high = width - 1
        
                while low <= high:
                    middle = low + (high - low)//2
                    mid_value = mat[row][middle]
                    
                    if target > mid_value:
                        low = middle + 1
                    elif target < mid_value:
                        high  =middle - 1
                    else:
                        return True
        return False
print(Solution.searchMatrix("", mat, 30))

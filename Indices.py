# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 12:06:14 2019

@author: Anuj
"""

A = [1,3,3,5,7,8,9,9,9,15]
x = 3
for x in A:
    f = A.index(x)
    for i in range(f, len(A)):
        if x==A[i]:
            L = [f,i]
        if x!=A[i]:
            print(f, i-1)
        print(L)
    else:
        print([-1,-1])
        
    
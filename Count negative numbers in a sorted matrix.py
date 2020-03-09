# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:50:36 2020

@author: Anuj
"""
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
count = 0
for i in grid:
    print(i)
    for innerindex in i:
        if innerindex < 0:
            count = count + 1
print(count)
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:49:00 2020

@author: Anuj
"""


n = 39

while n>10:
    sum1 = 0
    for i in str(n):
        sum1 = sum1 + int(i)
    n = sum1
print(sum1)
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:44:32 2020

@author: Anuj
"""
i = "hello"
vowel = ["a","e","i","o","u"]
vowelcount = False
for index in vowel:
    print(index)
    if index in i:
        vowelcount = True
    print(vowelcount)
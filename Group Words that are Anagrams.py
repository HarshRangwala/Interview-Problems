# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:24:44 2019

@author: Anuj
"""
import collections
anagram = []
for word_1 in l:
    print("WORD_1",word_1)
    for word_2 in l:
        print("WORD_2",word_2)
        if word_1!=word_2 and (sorted(word_1)==sorted(word_2)):
            anagram.append(word_1)
            break
anagram.append(word_2)
        
print(l)
d = collections.defaultdict(list)
for st in anagram:
    d[''.join(sorted(st))].append(st)
print(d.values())
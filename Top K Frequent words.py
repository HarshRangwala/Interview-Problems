# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:26:48 2019

@author: Anuj
"""
import collections
import heapq
class Solution(object):
  def topKFrequent(self, words, k):
    # Fill this in.
    C = collections.Counter(words) # count the number of distinct words

    pairs = [ (-val, key) for key, val in C.items() ] # I save the (key, val) pairs so that they are ready to be sorted
    # note that I only need to find the smallest k of them
    
    smallest_k = heapq.nsmallest(k, pairs) # heapq is a very handy module! nsmallest is a very handy function!
    
    return [p[1] for p in smallest_k]


words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
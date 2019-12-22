# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 20:19:59 2019

@author: Anuj
"""
class Solution(): 
     def __init__(self, p, i):
         self.p = 0
         self.i = 0
     def longestPalindrome(self, s):
         
          s = 'million'
          m = ''
          for i in range(len(s)):
              for j in range(len(s), i, -1):
                  if len(m) >= j-i:
                      break
                  else:
                      if s[i:j] == s[i:j][::-1] and len(s[i:j]) >= len(m):
                          m = s[i:j]
          return m 
            
print(Solution().longestPalindrome('million'))
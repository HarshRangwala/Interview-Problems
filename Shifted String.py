# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def is_shifted(a, b):
  # Fill this in.
  if len(a) != len(b):
      return False
  for index in range(len(a)):
      prev = a[:index]
      rem = a[index:]
      if rem+prev == b:
          return True
  return False  
print(is_shifted('abc', 'acb'))
# True
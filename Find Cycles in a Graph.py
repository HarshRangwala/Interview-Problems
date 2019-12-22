# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:04:50 2019

@author: Anuj
"""

def find_cycle(graph):
  # Fill this in.



graph = {
  'a': {'a2':{}, 'a3':{} },
  'b': {'b2':{}},
  'c': {}
}
print find_cycle(graph)
# False
graph['c'] = graph
print find_cycle(graph)
# True
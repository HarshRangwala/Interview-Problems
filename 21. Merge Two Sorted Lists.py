# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:59:49 2020

@author: Anuj
"""

def merge_list(list1, list2):
    if list1 is None:
        return list1
    if list2 is None:
        return list2
    if (list1.value < list2.value):
        list1.next = merge_list(list1.next, list2)
        return list1
    else:
        list2.next = merge_list(list2.next, list1)
        return list2

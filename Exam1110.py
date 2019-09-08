# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:58:12 2019

@author: Kwon
"""

n = input()
if len(n) < 2:
    n = '0' + n
    
m = ''
o = n
count = 0


while n != m:
    if count != 0:
        o = m
    
    res = str(int(o[0]) + int(o[1]))
    m = o[-1] + res[-1]
    count += 1
    
print(count)
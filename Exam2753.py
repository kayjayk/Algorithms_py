# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:20:36 2019

@author: Kwon
"""

year = int(input())

if year % 4 != 0 :
    print(0)
elif year % 100 == 0 :
    if year % 400 == 0 :
        print(1)
    else :
        print(0)
        
else :
    print(1)
    
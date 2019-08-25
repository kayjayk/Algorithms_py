# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:17:48 2019

@author: Kwon
"""

inputStr = input().split(" ")

A = int(inputStr[0])
B = int(inputStr[1])

if A > B :
    print('>')
elif A < B :
    print('<')
else :
    print('==')
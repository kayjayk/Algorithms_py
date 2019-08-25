# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:27:01 2019

@author: Kwon
"""

inputStr = input()
H = int(inputStr[0])
M = int(inputStr[1])

M -= 45

if M < 0 :
    H -= 1
    M += 60
    
if H < 0 :
    H += 24
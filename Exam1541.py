# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:53:07 2019

@author: Kwon
"""

inputStr = input()

splitedByMinus = inputStr.split('-')
minValue = 0

for i in range(len(splitedByMinus)) :
    splitedByPlus = splitedByMinus[i].split('+')
    
    for j in range(len(splitedByPlus)) :
        if i == 0 :
            minValue += int(splitedByPlus[j])
        
        else :
            minValue -= int(splitedByPlus[j])
            
print(minValue)
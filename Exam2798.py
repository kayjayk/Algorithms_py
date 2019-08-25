# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:53:38 2019

@author: Kwon
"""

inputStr = input().split(" ")
N = int(inputStr[0])
M = int(inputStr[1])

inputStr = input().split(" ")
numList = list()

for i in range(N) :
    numList.append(int(inputStr[i]))

maxValue = 0

for i in range(N) :
    for j in range(N) :
        for k in range(N) :
            if i == j or j == k or k == i :
                continue
        
            sumOfNums = numList[i] + numList[j] + numList[k]
            if sumOfNums > maxValue and sumOfNums <= M :
                maxValue = sumOfNums

print(maxValue)
                
            
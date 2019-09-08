# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:39:08 2019

@author: Kwon
"""

numList = input().split()
for i in range(len(numList)):
    numList[i] = int(numList[i])

numList.sort()
print(numList[1])
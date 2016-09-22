__author__ = "Sumanth_Lingappa"

import sys

def powerSet(s):
    sLen = len(s)
    numOfPowerSets = 1 << sLen # 2^n
    pSet = []
    for counter in range(numOfPowerSets):
        tempStr = ''
        for j in range(sLen):
            if counter & (1 << j):
                tempStr += s[j]
        pSet.append(tempStr)
    return sorted(pSet, key=len)


print powerSet('abc')

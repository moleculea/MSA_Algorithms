# -*- coding: utf-8 -*-
from math import *
from DIGIT import *

# Success Rate calculated by MSA
successRate = {20100312: 10, 20100909: 12, 20100311: 11}

# Temporary Data Begin
# Host's Daily Period Status within the Meeting Range
dailyPeriod = {
 20100312: 0b1100001111000011, 
 20100909: 0b1100001111000011, 
 20100311: 0b1100001111000011,
}

# Meeting Length
meetingLen = 2

# Preferred Period
preferredPeriod = 0b1111100000000011
# Temporary Data End

def sortSuccessRate(successRate):
    return sorted(successRate.iteritems(), key = lambda item:item[1], reverse = True)

def genDate(sortedSuccessRate):
    return sortedSuccessRate.pop(0) # Pop the first tuple in the list

def filterShortPeriod(dperiod, mLen): # modified from countZero()
    bitToOne = []
    cZero = 0 # Consecutive number of zeroes temporarily counted
    
    for i in range(0,16):
        if (dperiod | DIGIT[i]) == DIGIT[i]:
            cZero = cZero + 1
            bitToOne.append(i)
            if i == range(0,16)[-1] and cZero != 0:
                if cZero < mLen:
                    for b in bitToOne:
                        dperiod = dperiod | (REVERSE - DIGIT[b]) # filter the bits into one
        else:
            if cZero != 0:
                if cZero < mLen:
                    for b in bitToOne:
                        dperiod = dperiod | (REVERSE - DIGIT[b]) # filter the bits into one
                bitToOne = []
            cZero = 0
    return dperiod
"""
getRecomPeriod : Get Recommended Period
"""    
def getRecomPeriod(dailyPeriodHost, mLen, pPeriod, successRate):
    sortedSuccessRate = sortSuccessRate(successRate)
    gdate = genDate(sortedSuccessRate)
    dailyPeriod = dailyPeriodHost[gdate[0]] # Daily Period of the generated date (gdate[0])
    period = pPeriod | dailyPeriod # OR two periods to get common part (1111101111000011)
    period = filterShortPeriod(period, mLen) # Filter the Consecutive Sub-Periods whose length are smaller than the Meeting Length
    return period
    
if __name__ == "__main__":    
    resultPeriod = getRecomPeriod(dailyPeriod, 3, preferredPeriod, successRate)
    print bin(resultPeriod)
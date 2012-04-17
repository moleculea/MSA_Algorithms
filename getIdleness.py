# -*- coding: utf-8 -*-
"""
getIdleness.py

return idleness for a single day
"""
from math import *
from DIGIT import *


def countZero(number):
    tZero = 0 # Total number of zeroes counted
    cZero = 0 # Consecutive number of zeroes temporarily counted
    lenIdlePeriod = []
    for i in range(0,16):
        if (number | DIGIT[i]) == DIGIT[i]:
            tZero = tZero + 1
            cZero = cZero + 1
            if i == range(0,16)[-1] and cZero != 0:
                lenIdlePeriod.append(cZero)
        else:
            if cZero != 0:
                lenIdlePeriod.append(cZero)
            cZero = 0
    #print "Zero(es): ", tZero
    return lenIdlePeriod # list for the length of Idle Period, e.g. [3,2,6] (there are three Idle Periods on this day, the length of each being 3, 2 and 6 respectively)  

def idle(lenIdlePeriod, mLen): 
    idleness = 0
    for length in lenIdlePeriod:
        if (length - mLen + 1) >= 1:
            idleness += length - mLen + 1
        else:
            continue 
    #print "Idleness: ", idleness
    return idleness
        
"""
getIdleness()

"""
def getIdleness(dailyPeriod, mlen): # Argument: Daily Period and Meeting Length
    lenIdlePeriod = countZero(dailyPeriod)
    idleness = idle(lenIdlePeriod, mlen) # Calculate idleness with length of Idle Period and Meeting Length
    return idleness

if __name__ == "__main__":
    binaryDailyPeriod = 0b1110001111101000
    intDailyPeriod = int(binaryDailyPeriod)
    print intDailyPeriod
    print getIdleness(intDailyPeriod,3)
    """
    for digit in DIGIT:
        print digit,bin(digit)
        print bin(65535-digit)
    """     
    
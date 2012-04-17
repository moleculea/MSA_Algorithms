﻿# -*- coding: utf-8 -*-
"""
searchBias.py
Relevant algorithms used to decide search bias
"""

def getAverageIdleness(dayRange, user):
    sumIdleness = 0
    days = len(dayRange) # Number of days in dayRange
    for dp in retriveAgenda(dayRange, user): # retriveAgenda() query database to get this user's Daily Periods within the dayRange
        sumIdleness += getIdleness(dp, mlen) # sumIdleness is the sum of idleness for each day within the dayRange
    averageIdleness = sumIdleness/days # Average Idleness
    return averageIdleness

def getSearchBias(dayRange, method, delimit=None, averageidle=None): 
# method = DAY_LENGTH | AVERAGE_IDLE
# delimit = delimit_days | delimit_idleness
# averageidle = averageIdleness
    searchBias = "LINEAR_EARLY"
    
    if method == "DAY_LENGTH":
        if delimit == None:
            delimit = 5 # Number of days
        if len(dayRange) < delimit:
            searchBias = "LINEAR_EARLY"
        else:
            searchBias = "HIERARCHICAL"
    elif method == "AVERAGE_IDLE":
        if delimit == None:
            delimit = 5 # Idleness
        if averageidle < delimit:
            searchBias = "LINEAR_EARLY"
        else:
            searchBias = "HIERARCHICAL"
    return searchBias
        

if __name__ == "__main__":


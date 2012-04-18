# -*- coding: utf-8 -*-
"""
retriveAgenda.py
model program to fetch data from database
"""
import mysql.connector
from dbconfig import Config # dbconfig is for dbconfig.py
config = Config.dbinfo().copy() # Initialization

def retrieveAgenda(dayRange, userID):

    db = mysql.connector.Connect(**config)
    cursor = db.cursor()

    tb_user_agenda = "user_agenda"  # Table name of user agenda
    fn_daily_period = "daily_period" # Field name of daily period
    fn_date = "date" # Field name of date
    fn_user_id = "user_id" # Field name of user id
    
    for date in dayRange: 
        stdp = "SELECT `%s` FROM `%s` WHERE `%s`='%s' AND `%s`='%s'"%(fn_daily_period,tb_user_agenda,fn_date,date,fn_user_id,userID)
        cursor.execute(stdp)
        warnings = cursor.fetchwarnings()
        if warnings:
            print warnings
        rows = cursor.fetchall()
        for row in rows:
            yield row[0] # Yield daily period

    db.close()
    
if __name__ == "__main__":
    dayRange = ['20120303']
    userID = 1
    retrieveAgenda(dayRange,userID)
    #pass

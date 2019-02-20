# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 00:48:49 2019

@author: Ken

program name : determining the date "D/M/Y"
"""

today = "30/1/2016"

def us_date_style(today):
    date = list(today.split("/"))
    day, month, year = int(date[0]), int(date[1]), int(date[2])
    
    # day
    if day > 0 and day <= 31:
        day += 1
    else:
        print("'day' should be written between 1 to 31")
        return
    
    
    # month 
    # the day have already added by 1 
    if year % 4 == 0 and month == 2 and day == 31: # leap year 
        day = 1
        month += 1
    elif year % 4 != 0 and month == 2 and day == 30: # common year
        day = 1
        month += 1
    elif month in [1,3,5,6,8,10,12] and day == 32: # solar month of 31 days
        day = 1
        month += 1
    elif month in [4,7,9,11] and day == 31: # lunar month of 30 days
        day = 1 
        month += 1
    else:
        print("'month' should be written between 1 to 12")
        return
    
    # year 
    if month == 13 and day == 1:
        month = 1 
        year += 1
    date_new = "/".join([str(day),str(month),str(year)])
    
    return date_new

tomorrow = us_date_style(today)


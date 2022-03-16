# File: DaysInMonth.py
# Student: Lokprabhat Katasani
# UT EID: lrk646
# Course Name: CS303E
# 
# Date: 2/16/2022
# Description of Program: This program takes in a year and month and
# ouputs the name and number of day in that month.

#get inputs
year = int(input('Please enter a year: '))
monthnum = int(input('Please enter a month: '))


#if else statements to get the month name and number of days from
#inputs
if monthnum == 1:
    month = 'January'
    days = 31
elif monthnum == 2:
    month = 'Feburary'
#check if leap year
    if ((year%4)==0):
        days = 29
    else:
        days = 28
elif monthnum == 3:
    month = 'March'
    days = 31
elif monthnum == 4:
    month = 'April'
    days = 30
elif monthnum == 5:
    month = 'May'
    days = 31
elif monthnum == 6:
    month = 'June'
    days = 30
elif monthnum == 7:
    month = 'July'
    days = 31
elif monthnum == 8:
    month = 'August'
    days = 31
elif monthnum == 9:
    month = 'September'
    days = 30
elif monthnum == 10:
    month = 'October'
    days = 31
elif monthnum == 11:
    month = 'November'
    days = 30
elif monthnum == 12:
    month = 'December'
    days = 31

#display outputs
print(month, year, "has", days, "days")

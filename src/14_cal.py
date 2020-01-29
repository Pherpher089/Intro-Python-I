"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

from datetime import date
import time
import sys
import calendar
from datetime import datetime

month = input('Please enter the month as MM or 01 for January: ')
year = input('Please enter the year as YY or 20 for 2020: ')

if(month == ''):
    month = datetime.now().month
else:
    month = int(month)

if(year == ''):
    year = datetime.now().year
else:
    year = int(year)


def get_cal(year, month):
    print(calendar.month(year, month))


get_cal(year, month)

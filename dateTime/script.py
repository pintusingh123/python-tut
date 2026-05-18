# date and time module
# from datetime import date, datetime,time,timedelta
from datetime import datetime

date = datetime.now()
print(date.date()) #return date
print(date.time()) #return time
print(date.year) #return year
print(date.month) #return month
print(date.day) #return day
print(date.hour) #return hour
print(date.minute) #return minute

# formating date and time
print()
print(date.strftime("%d-%m-%Y %H:%M:%S %p")) # formating date and time

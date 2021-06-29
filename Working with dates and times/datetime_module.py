#Datetime object

import datetime

today = datetime.datetime(year=2019, month=12, day=23, hour=11, minute=49, second=30)
tomorrow = datetime.datetime(year=2019, month=12, day=24, hour=11, minute=49, second=30)
print(today > tomorrow)  # False

#getting and displaying todays date and time

import datetime

today = datetime.datetime.now()

print(today.strftime("%Y-%m-%d"))
# 2019-12-23

print(today.strftime("%H:%M"))
# 11:54

#converting string to datetime

import datetime

user_date = input("Enter today's date: ")
# Assume they entered 23-12-2019

today = datetime.datetime.strptime(user_date, "%d-%m-%Y")
print(today)  # 2019-12-23 00:00:00

#timestamps

import datetime

today = datetime.datetime.now()
print(today.timestamp())  # 1577104357.558527

import time

print(time.time())  # 1577104492.7515678
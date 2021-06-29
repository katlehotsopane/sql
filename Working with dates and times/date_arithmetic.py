#adding to time

import datetime

today = datetime.datetime.now()
one_week = datetime.timedelta(days=7)

print(today + one_week) # 2019-12-30 11:58:52.073407

#comparing datetime and timedelta

import datetime

user_date = input("When will you paint your shed? ")
redecorate_date = datetime.datetime.strptime(user_date, "%d-%m-%Y")

next_week = datetime.datetime.now() + datetime.timedelta(days=7)

if redecorate_date > next_week:
    print("You're not painting within the next week!")

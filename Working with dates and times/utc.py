#getting current date and time in utc

import datetime

today = datetime.datetime.now(datetime.timezone.utc)
print(today) # 2019-12-23 15:35:56.133138+00:00

#converting timezones using pytz

import pytz

eastern = pytz.timezone("US/Eastern")
amsterdam = pytz.timezone("Europe/Amsterdam")

#Adding timezone information to a native datetime

import datetime
import pytz

eastern = pytz.timezone("US/Eastern")

local_time = datetime.datetime.now()
print(local_time)  # 2020-02-12 11:47:21.817708
eastern_time = eastern.localize(local_time)
print(eastern_time)  # 2020-02-12 11:47:21.817708-05:00

#converting

import datetime
import pytz

eastern = pytz.timezone("US/Eastern")
amsterdam = pytz.timezone("Europe/Amsterdam")

local_time = datetime.datetime.now()
eastern_time = eastern.localize(local_time)
print(eastern_time)  # 2020-02-12 11:47:21.817708-05:00

amsterdam_time = eastern_time.astimezone(amsterdam)
print(amsterdam_time)  # 2020-02-12 17:47:21.817708+01:00

#getting current local time from users

import datetime
import pytz

local_time = datetime.datetime.now()
utc_local_time = datetime.datetime.now(tz=pytz.utc)

print(local_time)  
print(utc_local_time)  
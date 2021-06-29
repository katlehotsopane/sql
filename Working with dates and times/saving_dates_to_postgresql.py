#saving dates to a json file

import pytz
import json

user_timezone = input("Enter your timezone: ").strip()

try:
    pytz.timezone(user_timezone)
except pytz.exceptions.UnknownTimeZoneError:
    print("That was not a valid timezone.")
    raise

with open("user_config.json", "w") as config:
    json.dump({"timezone": user_timezone}, config)

#saving dates to a database

import datetime
import pytz
import psycopg2

connection = psycopg2.connect("...")
# This would come from database or config file
user_timezone = pytz.timezone("Europe/London")

new_post_content = input("Enter what you learned today: ")
# Instead of `.now()`, we could ask users for a local date and time
new_post_date = user_timezone.localize(datetime.datetime.now())
utc_post_date = new_post_date.astimezone(pytz.utc)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO posts (content, date) VALUES (%s, %s)",
            (new_post_content, utc_post_date.timestamp())
        )

#reading dates from database

import datetime
import pytz
import psycopg2

connection = psycopg2.connect("...")
# This would come from database or config file
user_timezone = pytz.timezone("Europe/London")

with connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM posts;")
        for post in cursor:
            _id, content, timestamp = post
            naive_datetime = datetime.utcfromtimestamp(timestamp)
            utc_date = pytz.utc.localize(naive_datetime)
            local_date = utc_date.astimezone(user_timezone)
            print(local_date)
            print(content) 
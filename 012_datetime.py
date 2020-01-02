from datetime import date, time, datetime
# 'pytz' is a Python 3 timezone package
import pytz

# NOTE: Last field is microseconds (millionths of a second), not milliseconds!
my_time = time(23, 59, 59, 999999)
print(my_time)
print("my time object has values | hour: {} | min: {} | sec: {} | microsec: {}"
      .format(my_time.hour, my_time.minute, my_time.second, my_time.microsecond))

my_date = date(2019, 12, 25)
print(my_date)
print("my date object has values | year: {} | month: {} | day: {}"
      .format(my_date.year, my_date.month, my_date.day))
date_today = date.today()
print("today's date is: {}".format(date_today))
christmas_this_year = date_today.replace(month=12, day=25)
print("Christmas this year is: {}".format(christmas_this_year))
my_timedelta = christmas_this_year - date_today
print("Christmas is {} days away!".format(my_timedelta.days))

now_without_timezone = datetime.now()
print("Current date/time without timezone: {}".format(now_without_timezone))
# fun with date/time formatting strings
print(now_without_timezone.strftime("%Y-%m-%d %H:%M and %S seconds!"))
# A datetime object without any timezone info in called 'naive' in Python terms.
# The next line should output 'None', since datetime.now() should return a naive object.
print(now_without_timezone.tzinfo)

dt_now_naive = datetime.now()
timezone_los_angeles = pytz.timezone("America/Los_Angeles")
timezone_halifax = pytz.timezone("America/Halifax")
dt_now_aware_los_angeles = timezone_los_angeles.localize(dt_now_naive)
dt_now_aware_halifax = timezone_halifax.localize(dt_now_naive)
dt_now_aware_utc = pytz.utc.localize(dt_now_naive)
print(dt_now_aware_los_angeles)
print(dt_now_aware_halifax)
print(dt_now_aware_utc)

# The 'datetime' class is able to create a 'now' datetime in UTC timezone via a static function
dt_now_utc_aware = datetime.utcnow()
print(dt_now_aware_utc)

# 'datetime' objects can output their time in ISO format
print(dt_now_naive.isoformat())
print(dt_now_aware_halifax.isoformat())
print(dt_now_aware_utc.isoformat())

# A timezone aware datetime can be converted to a different timezone
dt_now_aware_newyork = dt_now_aware_halifax.astimezone(pytz.timezone("America/New_York"))
print("current time | Halifax: {} | New York: {} | (timezones should be one hour apart)"
      .format(dt_now_aware_halifax.isoformat(), dt_now_aware_newyork.isoformat()))

import pytz
from datetime import datetime

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
   in_zone = []
   for timezone in timezones:
      if timezone not in TIMEZONES:
         raise ValueError
      location = pytz.timezone(timezone)
      utc_dt = pytz.utc.localize(utc)
      location_dt = utc_dt.astimezone(location)
      if location_dt.hour in MEETING_HOURS:
         in_zone.append(1)
   return True if len(in_zone) == len(timezones) else False




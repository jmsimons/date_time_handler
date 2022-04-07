import datetime, time
from pytz import timezone



tz_pac = timezone("US/Pacific")
tz_utc = timezone("UTC")

start_tuple = (2000, 1, 1, 0, 0, 0)
naive_time_obj = datetime.datetime(*start_tuple, tzinfo = None)
pac_time_obj = tz_pac.localize(naive_time_obj)
utc_time_obj = pac_time_obj.astimezone(tz_utc)
naive_seconds = int(naive_time_obj.strftime("%s"))
pac_seconds = int(pac_time_obj.strftime("%s"))
utc_seconds = int(utc_time_obj.strftime("%s"))
print("Naive\tseconds:", naive_seconds, "\ttimestamp:", naive_time_obj.timestamp(), "\trepr:", naive_time_obj)
print("PAC\tseconds:", pac_seconds, "\ttimestamp:", pac_time_obj.timestamp(), "\trepr:", pac_time_obj)
print("UTC\tseconds:", utc_seconds, "\ttimestamp:", utc_time_obj.timestamp(), "\trepr:", utc_time_obj)
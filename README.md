# date-time-handler
Robust date-time formatter with implicit time-zone conversion 

- Uses Python standard library time and datetime
- Requires pytz and dateutil to be installed:
    $ pip3 install pytz
    $ pip3 install python-dateutil
- date_time_handler package contains class DateTimeHandler with methods that convert timestamp format and time-zone
- By default, DateTimeHandler performs timezone-naive timestamp format conversion
- For implicit timezone conversion:
    - set destination tz with kwarg time_zone = 'region/zone' at instantiation
    - then kwarg start_tz = 'region/zone' when converting timestamp format
- All methods take timestamp in any format: int/float, tuple/struct, formatted_string

### examples: go ahead, give 'em a try ###
```
>>> ### for time-zone agnostic format conversion ###
>>> dt_format = DateTimeHandler()
>>> timestring = dt_format.timestring(timestamp)
>>> time_tuple = dt_format.timetuple(timestamp)
>>> datestamp = dt_format.datestamp(timestamp)
```
```
>>> ### for time-zone conversion, set destination tz at instantiation ###
>>> dt_format = DateTimeHandler(time_zone = 'US/Pacific')
```
```
>>> ### specify starting timezone when converting timestamp ###
>>> local_timestamp = dt_format.timestamp(utc_timestamp, start_tz = 'UTC')
>>> local_timestring = dt_format.timestring(utc_timestamp, start_tz = 'UTC')
>>> local_timetuple = dt_format.timetuple(utc_timestamp, start_tz = 'UTC')
```
```
>>> ### so-called 'date' methods return the given timestamp's date @ 00:00:00 ###
>>> local_datestamp = dt_format.datestamp(utc_timestamp, start_tz = 'UTC')
>>> local_datestring = dt_format.datestring(utc_timestamp, start_tz = 'UTC')
>>> local_datetuple = dt_format.datetuple(utc_timestamp, start_tz = 'UTC')
```
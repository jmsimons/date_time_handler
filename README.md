# date-time-handler
Robust date-time formatter with implicit time-zone conversion 

- Uses Python standard library time and datetime
- Requires pytz and dateutil to be installed:
    $ pip3 install pytz
    $ pip3 install python-dateutil
- date_time_handler package contains class DateTimeHandler with methods that convert timestamp format and time-zone
- all methods take timestamp in any format: int/float, tuple/struct, formated_string

>>> ### for time-zone agnostic format conversion ###
>>> dt_format = DateTimeHandler()
>>> timestring = dt_format.timestring(timestamp)
>>> time_tuple = dt_format.timetuple(timestamp)
>>> datestamp = dt_format.datestamp(timestamp)
>>>
>>> ### set destination time-zone at instantiation, defaults to utc ###
>>> dt_format = DateTimeHandler(time_zone = 'US/Pacific')
>>>
>>> ### specify starting timezone when converting timestamp, defaults to utc ###
>>> local_timestamp = dt_format.timestamp(utc_timestamp, start_tz = 'UTC')
>>> local_timestring = dt_format.timestring(utc_timestamp, start_tz = 'UTC')
>>> local_timetuple = dt_format.timetuple(utc_timestamp, start_tz = 'UTC')
>>> 
>>> ### so-called 'date' methods return the given timestamp's date @ 00:00:00 ###
>>> local_datestamp = dt_format.datestamp(utc_timestamp, start_tz = 'UTC')
>>> local_datestring = dt_format.datestring(utc_timestamp, start_tz = 'UTC')
>>> local_datetuple = dt_format.datetuple(utc_timestamp, start_tz = 'UTC')
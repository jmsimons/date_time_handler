# date-time-handler
## Robust date-time formatter with implicit time-zone conversion ##
### Out of the box solution for quick and easy proto-type building ###


- Uses Python standard library time and datetime
- Requires pytz and dateutil to be installed:
```
    $ pip3 install pytz
    $ pip3 install python-dateutil
```
- date_time_handler package contains class DateTimeHandler with methods that convert timestamp format and time-zone
- By default, DateTimeHandler performs timezone-naive timestamp format conversion (handy for quick display formatting)
- For implicit timezone conversion:
    - set destination tz with kwarg ```time_zone = 'region/local'``` at instantiation
    - then kwarg ```start_tz = 'region/local'``` when converting timestamp format
- All methods take 'timestamp' in any format: int/float, tuple/struct, formatted_string, and even datetime obj


### examples ###

#### for time-zone agnostic format conversion ####
```
>>> dt_format = DateTimeHandler(date_format = "%Y/%m/%d", clock_format = "%H:%M:%S")
>>> timestring = dt_format.timestring(timestamp)
>>> timetuple = dt_format.timetuple(timestamp)
>>> datestamp = dt_format.datestamp(timestamp)
```

#### for time-zone conversion, set destination tz at instantiation ####
```
>>> dt_format = DateTimeHandler(time_zone = 'US/Pacific')

    # specify starting timezone when converting timestamp #
>>> local_timestring = dt_format.timestring(utc_timestamp, start_tz = 'UTC')
>>> local_timetuple = dt_format.timetuple(utc_timestamp, start_tz = 'UTC')
```

#### so-called 'date' methods return the given timestamp's date @ 00:00:00 ####
```
>>> local_datestring = dt_format.datestring(utc_timestamp, start_tz = 'UTC')
>>> local_datetuple = dt_format.datetuple(utc_timestamp, start_tz = 'UTC')
```
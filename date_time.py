import time, datetime, dateutil, pytz
from time import struct_time
from pytz import timezone
from dateutil.relativedelta import relativedelta


def load_tz(time_zone):
    ''' Safely creates and returns a timezone object '''
    try:
        tz = timezone(time_zone)
    except pytz.exceptions.UnknownTimeZoneError:
        tz = None
    return tz


class DateTimeHandler:

    '''
    - This class contains convenience methods for timestamp formatting.
    '''

    def __init__(self, date_format = "%Y/%m/%d", clock_format = "%H:%M:%S", time_zone = "UTC"):
        self.time_zone = load_tz(time_zone)
        self.date_format = date_format
        self.clock_format = clock_format
        self.time_format = f"{date_format} {clock_format}"

    def _get_time_obj(self, time_stamp, start_tz = "UTC"):
        ''' Takes time_stamp in seconds, tuple, or string and returns a datetime object '''
        if type(time_stamp) == float or type(time_stamp) == int:
            time_obj = datetime.datetime.fromtimestamp(time_stamp)
        elif type(time_stamp) == tuple or type(time_stamp) == struct_time:
            time_obj = datetime.datetime(*time_stamp) # unpack time_stamp tuple as datetime arguments
        elif type(time_stamp) == str:
            time_obj = datetime.datetime.strptime(time_stamp, self.time_format)
        timezone(start_tz).localize(time_obj)
        if self.time_zone:
            time_obj = time_obj.astimezone(self.time_zone)
        return time_obj

    def timestring(self, time_stamp, **kwargs):
        ''' Gets datetime object with time_stamp and returns a formated datetime string '''
        time_obj = self._get_time_obj(time_stamp, **kwargs)
        return time_obj.strftime(self.time_format)
    
    def timestamp(self, time_stamp, **kwargs):
        ''' Gets datetime object with time_stamp and returns seconds since the epoch '''
        time_obj = self._get_time_obj(time_stamp, **kwargs)
        return time_obj.timestamp()
    
    def timetuple(self, time_stamp, **kwargs):
        ''' Gets datetime object with time_stamp and returns a datetime tuple '''
        time_obj = self._get_time_obj(time_stamp, **kwargs)
        return time_obj.timetuple()
    
    def datestring(self, time_stamp, **kwargs):
        ''' Gets datetime object with time_stamp and returns a formated date string '''
        date_obj = self._get_time_obj(time_stamp, **kwargs)
        date_str = date_obj.strftime(self.date_format)
        return date_str
    
    def datestamp(self, time_stamp, **kwargs):
        ''' Gets datetime object with time_stamp and returns date at 00:00 in seconds since the epoch '''
        date_obj = self._get_time_obj(time_stamp, **kwargs)
        date_obj = date_obj.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
        return date_obj.timestamp()
    
    def datetuple(self, time_stamp, **kwargs):
        ''' Gets datetime object with time_stamp and returns a date tuple '''
        date_obj = self._get_time_obj(time_stamp, **kwargs)
        date_obj = date_obj.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
        return date_obj.timetuple()

    def add_interval(self, time_stamp, interval):
        ''' Returns time_stamp + specified interval in seconds '''
        time_obj = self._get_time_obj(time_stamp)
        if interval == "daily":
            time_obj += datetime.timedelta(days = 1)
        elif interval == "weekly":
            time_obj += datetime.timedelta(weeks = 1)
        elif interval == "monthly":
            time_obj += relativedelta(months = 1)
        elif interval == "3 months":
            time_obj += relativedelta(months = 3)
        elif interval == "6 months":
            time_obj += relativedelta(months = 6)
        elif interval == "12 months":
            time_obj += relativedelta(months = 12)
        return time_obj.timestamp()
